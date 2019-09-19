# -*- coding: utf-8 -*-
##
# Copyright (c) 2017 Ivan Semkin.
#
# This file is part of VK-Scraper
# (see https://github.com/vanyasem/VK-Scraper).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##

import argparse
import concurrent.futures
import errno
import glob
import logging
import os
import re
import sys
import textwrap
import time

import requests
import tqdm
import vk_api
import youtube_dl


class VkScraper(object):
    """VkScraper scrapes and downloads an VK user's photos, saved pictures, videos, and stories"""

    def __init__(self, **kwargs):
        self.maximum = None
        self.media_types = None
        self.latest = None
        self.retain_username = None
        self.destination = None
        self.quiet = None
        self.usernames = None
        self.login_pass = None
        self.login_user = None

        default_attr = dict(username='', usernames=[], filename=None,
                            login_user=None, login_pass=None,
                            destination='./', retain_username=False,
                            quiet=False, maximum=0,
                            latest=False,
                            media_types=['image'],
                            verbose=0,
                            )

        allowed_attr = list(default_attr.keys())
        default_attr.update(kwargs)

        for key in default_attr:
            if key in allowed_attr:
                self.__dict__[key] = kwargs.get(key)

        # Set up a logger
        self.logger = VkScraper.get_logger(level=logging.DEBUG,
                                           verbose=default_attr.get('verbose'))

        self.session = requests.Session()

        self.logged_in = False
        self.vk = None
        self.vk_session = None
        self.tools = None
        self.last_scraped_file_time = 0

    def login(self):
        """Logs in to VK"""
        self.vk_session = vk_api.VkApi(
            self.login_user, self.login_pass,
            auth_handler=self.two_factor_handler,
            captcha_handler=self.captcha_handler,
            app_id=6036185,
            api_version='5.101',
        )

        try:
            self.vk_session.auth()
            self.logged_in = True
        except vk_api.AuthError as error_msg:
            print(error_msg)
            self.logger.error('Login failed for ' + self.login_user)
            return

        self.vk = self.vk_session.get_api()
        self.tools = vk_api.VkTools(self.vk_session)

    @staticmethod
    def two_factor_handler():
        key = input("Enter authentication code: ")
        remember_device = True

        return key, remember_device

    @staticmethod
    def captcha_handler(captcha):
        key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

        return captcha.try_again(key)

    @staticmethod
    def get_logger(level=logging.DEBUG, verbose=0):
        """Returns a logger"""
        logger = logging.getLogger(__name__)

        fh = logging.FileHandler('vk-scraper.log', 'w')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        fh.setLevel(level)
        logger.addHandler(fh)

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        sh_levels = [logging.ERROR, logging.WARNING, logging.INFO]
        sh.setLevel(sh_levels[verbose])
        logger.addHandler(sh)

        return logger

    @staticmethod
    def parse_file_usernames(usernames_file):
        """Parses a file containing a list of usernames"""
        users = []

        try:
            with open(usernames_file) as user_file:
                for line in user_file.readlines():
                    # Find all usernames delimited by ,; or whitespace
                    users += re.findall(r'[^,;\s]+', line.split("#")[0])
        except IOError as err:
            raise ValueError('File not found ' + err)
        return users

    @staticmethod
    def parse_delimited_str(inp):
        """Parse the string input as a list of delimited tokens"""
        return re.findall(r'[^,;\s]+', inp)

    def scrape(self, executor=concurrent.futures.ThreadPoolExecutor(max_workers=10)):
        """Crawls through and downloads user's media"""
        if self.login_user and self.login_pass:
            self.login()
            if not self.logged_in:
                self.logger.warning('Fallback anonymous scraping disabled')
                return

        for username in self.usernames:
            self.last_scraped_file_time = 0
            future_to_item = {}

            dst = self.make_dst_dir(username)

            # Get the user metadata.
            try:
                user_id = self.check_user(username)
            except:
                print('Error getting user details for {0}'.format(username))
                continue

            if user_id:
                self.get_photos(dst, executor, future_to_item, user_id)
                self.get_saved(dst, executor, future_to_item, user_id)
                self.get_videos(dst, executor, future_to_item, user_id)
                self.get_stories(dst, executor, future_to_item, user_id)

            # Displays the progress bar of completed downloads. Might not even pop up if all media is downloaded while
            # the above loop finishes.
            if future_to_item:
                for future in tqdm.tqdm(concurrent.futures.as_completed(future_to_item),
                                        total=len(future_to_item), desc='Downloading', disable=self.quiet):
                    item = future_to_item[future]

                    if future.exception() is not None:
                        self.logger.warning(
                            '\nMedia with ID {0} generated an exception: {1}'.format(item['id'], future.exception()))


    def make_dst_dir(self, username):
        """Creates the destination directory."""
        if self.destination == './':
            destination = './' + username
        else:
            if self.retain_username:
                destination = self.destination + '/' + username
            else:
                destination = self.destination

        try:
            os.makedirs(destination)
        except OSError as err:
            if err.errno == errno.EEXIST and os.path.isdir(destination):
                # Directory already exists
                self.get_last_scraped_file_time(destination)
                pass
            else:
                # Target dir exists as a file, or a different error
                raise

        return destination

    def get_last_scraped_file_time(self, dst):
        """Stores the last modified time of newest file in a directory."""
        list_of_files = []
        file_types = ('*.jpg', '*.mp4')

        for file_type in file_types:
            list_of_files.extend(glob.glob(dst + '/' + file_type))

        if list_of_files:
            latest_file = max(list_of_files, key=os.path.getmtime)
            self.last_scraped_file_time = int(os.path.getmtime(latest_file))

    def check_user(self, username):
        """Checks whether a user or community exists"""
        try:
            response = self.vk.users.get(user_ids=username)
            if response:
                try:
                    return response[0]['id']
                except:
                    raise ValueError('User {0} does not exist'.format(username))
        except vk_api.exceptions.ApiError:
            response = self.vk.groups.getById(group_id=-int(username))
            if response:
                try:
                    return -response[0]['id']
                except:
                    raise ValueError('Community {0} does not exist'.format(username))
            else:
                raise ValueError('Community {0} does not exist'.format(username))

    def is_new_media(self, item):
        """Returns True if the media is new"""
        return self.latest is False or self.last_scraped_file_time == 0 or \
            ('date' not in item) or item.get('date') > self.last_scraped_file_time

    @staticmethod
    def determine_max_media_res(item, save_dir):
        if 'duration' in item:  # Video
            return VkScraper.determine_max_video_res(item, save_dir)
        elif 'video' in item and 'duration' in item['video']:  # Video story
            return VkScraper.determine_max_video_res(item['video'], save_dir)
        elif 'sizes' in item:  # Photo
            return VkScraper.determine_max_photo_res(item)
        elif 'photo' in item and 'sizes' in item['photo']:  # Photo story
            return VkScraper.determine_max_photo_res(item['photo'])

    class VideoLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print('\n' + msg)

    @staticmethod
    def determine_max_video_res(item, save_dir):
        if 'files' in item:
            if 'mp4_1080' in item['files']:
                return item['files']['mp4_1080']
            if 'mp4_720' in item['files']:
                return item['files']['mp4_720']
            if 'mp4_480' in item['files']:
                return item['files']['mp4_480']
            if 'mp4_360' in item['files']:
                return item['files']['mp4_360']
            if 'mp4_240' in item['files']:
                return item['files']['mp4_240']
        elif 'player' in item:  # TODO: parse VK videos here to download user-owned private files
            ydl_opts = {
                'outtmpl': save_dir + '/%(title)s.%(ext)s',
                'noplaylist': True,
                'logger': VkScraper.VideoLogger(),
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([item['player']])

    @staticmethod
    def determine_max_photo_res(item):
        sizes = []
        for size in item['sizes']:
            sizes.append(size['type'])
        if 'w' in sizes:
            return item['sizes'][sizes.index('w')]['url']
        elif 'z' in sizes:
            return item['sizes'][sizes.index('z')]['url']
        elif 'y' in sizes:
            return item['sizes'][sizes.index('y')]['url']
        elif 'x' in sizes:
            return item['sizes'][sizes.index('x')]['url']
        elif 'm' in sizes:
            return item['sizes'][sizes.index('m')]['url']
        elif 's' in sizes:
            return item['sizes'][sizes.index('s')]['url']

    def download(self, item, save_dir='./'):
        """Downloads the media file"""
        url = self.determine_max_media_res(item, save_dir)
        base_name = url.split('/')[-1].split('?')[0]
        file_path = os.path.join(save_dir, base_name)

        if not os.path.isfile(file_path):
            with open(file_path, 'wb') as media_file:
                try:
                    content = self.session.get(url).content
                except requests.exceptions.ConnectionError:
                    time.sleep(5)
                    content = self.session.get(url).content

                media_file.write(content)

            file_time = item.get('date', time.time())
            os.utime(file_path, (file_time, file_time))

    def photos_gen(self, user_id):
        """Generator of all user's photos"""
        try:
            photos = self.tools.get_all('photos.getAll', 200, {'owner_id': user_id})

            for item in photos['items']:
                yield item
        except ValueError:
            self.logger.exception('Failed to get photos for ' + user_id)

    def get_photos(self, dst, executor, future_to_item, username):
        """Scrapes the user's albums for photos"""
        if 'image' not in self.media_types:
            return

        iterator = 0
        for item in tqdm.tqdm(self.photos_gen(username), desc='Searching {0} for photos'.format(username),
                              unit=' photos', disable=self.quiet):
            if self.is_new_media(item):
                future = executor.submit(self.download, item, dst)
                future_to_item[future] = item

            iterator += 1
            if self.maximum != 0 and iterator >= self.maximum:
                break

    def saved_gen(self, user_id):
        """Generator of all user's saved pictures"""
        try:
            photos = self.tools.get_all('photos.get', 200, {'owner_id': user_id, 'album_id': 'saved'})

            for item in photos['items']:
                yield item
        except ValueError:
            self.logger.exception('Failed to get saved pictures for ' + user_id)

    def get_saved(self, dst, executor, future_to_item, username):
        """Scrapes the user's saved pictures for photos"""
        if 'saved' not in self.media_types:
            return

        iterator = 0
        for item in tqdm.tqdm(self.saved_gen(username), desc='Searching {0} for saved pictures'.format(username),
                              unit=' pictures', disable=self.quiet):
            if self.is_new_media(item):
                future = executor.submit(self.download, item, dst)
                future_to_item[future] = item

            iterator += 1
            if self.maximum != 0 and iterator >= self.maximum:
                break

    def videos_gen(self, user_id):
        """Generator of all user's videos"""
        try:
            videos = self.tools.get_all('video.get', 200, {'owner_id': user_id})

            for item in videos['items']:
                if item['owner_id'] == user_id:
                    yield item

        except ValueError:
            self.logger.exception('Failed to get videos for ' + user_id)

    def get_videos(self, dst, executor, future_to_item, username):
        """Scrapes the user's videos"""
        if 'video' not in self.media_types:
            return

        iterator = 0
        for item in tqdm.tqdm(self.videos_gen(username), desc='Searching {0} for videos'.format(username),
                              unit=' videos', disable=self.quiet):
            if self.is_new_media(item):
                future = executor.submit(self.download, item, dst)
                future_to_item[future] = item

            iterator += 1
            if self.maximum != 0 and iterator >= self.maximum:
                break

    def stories_gen(self, user_id):
        """Generator of user's stories"""
        try:
            stories = self.tools.get_all('stories.get', 200, {'owner_id': user_id})

            for item in stories['items'][0]:
                yield item
        except ValueError:
            self.logger.exception('Failed to get stories for ' + user_id)

    def get_stories(self, dst, executor, future_to_item, username):
        """Scrapes the user's stories"""
        if 'story' not in self.media_types:
            return

        iterator = 0
        for item in tqdm.tqdm(self.stories_gen(username), desc='Searching {0} for stories'.format(username),
                              unit=' stories', disable=self.quiet):
            if self.is_new_media(item):
                future = executor.submit(self.download, item, dst)
                future_to_item[future] = item

            iterator += 1
            if self.maximum != 0 and iterator >= self.maximum:
                break


def main():
    parser = argparse.ArgumentParser(
        description="VK-Scraper scrapes and downloads an VK user's photos and videos.",
        epilog=textwrap.dedent("""
            You can hide your credentials from the history, by reading your
            username from a local file:
            $ vk-scraper @vk_args.txt user_to_scrape
            with vk_args.txt looking like this:
            -u=my_username
            -p=my_password
            You can add all arguments you want to that file, just remember to have
            one argument per line.
            """),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        fromfile_prefix_chars='@')

    parser.add_argument('username', help='VK user(s) to scrape', nargs='*')
    parser.add_argument('--destination', '-d', default='./', help='Download destination')
    parser.add_argument('--login-user', '--login_user', '-u', default=None, help='VK username')
    parser.add_argument('--login-pass', '--login_pass', '-p', default=None, help='VK password')
    parser.add_argument('--filename', '-f', help='Path to a file containing a list of users to scrape')
    parser.add_argument('--quiet', '-q', default=False, action='store_true', help='Be quiet while scraping')
    parser.add_argument('--maximum', '-m', type=int, default=0, help='Maximum number of items to scrape')
    parser.add_argument('--retain-username', '--retain_username', '-n', action='store_true', default=False,
                        help='Creates username subdirectory when destination flag is set')
    parser.add_argument('--media-types', '--media_types', '-t', nargs='+',
                        default=['image'],
                        help='Specify media types to scrape')
    parser.add_argument('--latest', action='store_true', default=False, help='Scrape new media since the last scrape')
    parser.add_argument('--verbose', '-v', type=int, default=0, help='Logging verbosity level')

    args = parser.parse_args()

    if args.login_user is None or args.login_pass is None:
        parser.print_help()
        raise ValueError('You must provide both username and password')

    if not args.username and args.filename is None:
        parser.print_help()
        raise ValueError('You must either provide username(s) or a file containing username(s)')
    elif args.username and args.filename:
        parser.print_help()
        raise ValueError('You must either provide username(s) OR a file containing username(s)')


    if args.filename:
        args.usernames = VkScraper.parse_file_usernames(args.filename)
    else:
        args.usernames = VkScraper.parse_delimited_str(','.join(args.username))

    if args.media_types and len(args.media_types) == 1 and re.compile(r'[,;\s]+').findall(args.media_types[0]):
        args.media_types = VkScraper.parse_delimited_str(args.media_types[0])

    scraper = VkScraper(**vars(args))

    scraper.scrape()


if __name__ == '__main__':
    main()
