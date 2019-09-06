VK Scraper
=================
![Python 2.6, 2.7, 3.4, 3.5, 3.6](https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.4%2C%203.5%2C%203.6-blue.svg)
[![GitHub License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://raw.githubusercontent.com/vanyasem/VK-Scraper/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/vk-scraper.svg)](https://pypi.python.org/pypi/VK-Scraper)
[![AUR](https://repology.org/badge/version-for-repo/aur/vk-scraper.svg)](https://aur.archlinux.org/packages/vk-scraper)
[![Travis](https://img.shields.io/travis/vanyasem/VK-Scraper.svg)](https://travis-ci.org/vanyasem/VK-Scraper)

vk-scraper is a command-line application written in Python that scrapes and downloads VK user's / community's data. Use responsibly.

Inspired by [instagram-scraper](https://github.com/rarcega/instagram-scraper)

Features
--------
- Scrape user's photos
- Scrape user's uploaded VK videos
- Scrape user's saved photos
- Scrape user's external videos thumbnails
- Scrape user's stories (`story` scrapes just the last one, `storybrute` also tries to bruteforce IDs of older stories)

Install
-------

#### Arch GNU/Linux
For the stable version:

    $ trizen -S vk-scraper

For the git version:

    $ trizen -S vk-scraper-git

#### Other distros
For the stable version:

    $ pip3 install vk-scraper --upgrade --user

For the git version:

    $ pip3 install git+https://github.com/vanyasem/VK-Scraper.git --upgrade --user

Usage
-----
To scrape user's media:
```bash
vk-scraper <username> -u <your username> -p <your password>
```
*By default, downloaded media will be placed in `<current working directory>/<username>`.*

To specify multiple users, pass a delimited list of users:
```bash
vk-scraper username1,username2,username3
```

You can also supply a file containing a list of usernames:
```bash
vk-scraper -f vk_users.txt
```

```
# vk_users.txt

username1
username2
username3

# and so on...
```
*Usernames may be separated by newlines, commas, semicolons, or whitespace.*

Arguments
---------
```
--help -h             Show help message and exit

--login-user  -u      VK username

--login-pass  -p      VK password

--filename    -f      Path to a file containing a list of users / communities to scrape

--destination -d      Specify the download destination. By default, media will
                      be downloaded to <current working directory>/<username>

--retain-username -n  Creates a username subdirectory when the destination flag is set

--media-types -t      Specify media types to scrape. Enter as space separated values.
                      Valid values are image, saved, video, story, storybrute or none
                      (defaults to image and video)

--latest              Scrape only new media since the last scrape. Uses the last modified
                      time of the latest media item in the destination directory to compare

--quiet       -q      Be quiet while scraping

--maximum     -m      Maximum number of items to scrape
```

Develop
-------
Clone the repo and create a virtualenv
```bash
virtualenv env
source env/bin/activate
python setup.py install
```

Contributing
------------
1. Check open issues or open a new one to start a discussion around
   your idea or a bug you found
2. Fork the repository and make your changes
3. Send a pull request

Futurelog
---------
- Add unit-tests
- Scrape by hashtag
- Scrape by location
- Save metadata to a file (likes, comments, etc)
- Sort photos by their albums
