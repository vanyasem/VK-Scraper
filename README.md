VK Scraper
=================
![Python 2.6, 2.7, 3.4, 3.5, 3.6](https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.4%2C%203.5%2C%203.6-blue.svg)
[![GitHub License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://raw.githubusercontent.com/vanyasem/VK-Scraper/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/vk-scraper.svg)](https://pypi.python.org/pypi/VK-Scraper)
[![Travis](https://img.shields.io/travis/vanyasem/VK-Scraper.svg)](https://travis-ci.org/vanyasem/VK-Scraper)

vk-scraper is a command-line application written in Python that scrapes and downloads VK user's / community's photos and videos. Use responsibly.

Inspired by [instagram-scraper](https://github.com/rarcega/instagram-scraper).

Install
-------
To install or update vk-scraper:
```bash
pip install vk-scraper --upgrade
```

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
*The usernames may be separated by newlines, commas, semicolons, or whitespace.*

OPTIONS
-------
```
--help -h             Show help message and exit

--login-user  -u      VK username

--login-pass  -p      VK password

--filename    -f      Path to a file containing a list of users / communities to scrape

--destination -d      Specify the download destination. By default, media will
                      be downloaded to <current working directory>/<username>

--retain-username -n  Creates a username subdirectory when the destination flag is set

--media-types -t      Specify media types to scrape. Enter as space separated values.
                      Valid values are image, video, or none

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

Futurelog:
-------
- Scrape by hashtag
- Scrape by location
- Save metadata to file
- ~~Scrape stories~~ Stories API is private. The only way to get them would be to parse vk.com.
- Sort photos by their albums
