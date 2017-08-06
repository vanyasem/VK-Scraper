VK Scraper
=================
![Python 2.6, 2.7, 3.4, 3.5, 3.6](https://img.shields.io/badge/python-2.6%2C%202.7%2C%203.4%2C%203.5%2C%203.6-blue.svg)
[![GitHub License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://raw.githubusercontent.com/vanyasem/VK-Scraper/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/vk-scraper.svg)](https://pypi.python.org/pypi/VK-Scraper)
[![Travis](https://img.shields.io/travis/vanyasem/VK-Scraper.svg)](https://travis-ci.org/vanyasem/VK-Scraper)

Inspired by [instagram-scraper](https://github.com/rarcega/instagram-scraper).

Install
-------
To install or update vk-scraper:
```bash
pip install instagram-scraper --upgrade
```

Develop
-------
Clone the repo and create a virtualenv 
```bash
virtualenv env
source env/bin/activate
python setup.py install
```

Futurelog:
-------
- Scrape by hashtag
- Scrape by location
- Save metadata to file
- ~~Scrape stories~~ Stories API is private. The only way to get them would be to parse vk.com.
- ~~Scrape videos~~ Video links are private, too. Parsing them would be easier, though.
- Sort photos by their albums
