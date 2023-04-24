VK Scraper
==========
![Python 3.5, 3.6, 3.7](https://img.shields.io/pypi/pyversions/vk_scraper.svg)
[![PyPI](https://img.shields.io/pypi/v/vk-scraper.svg)](https://pypi.python.org/pypi/VK-Scraper)
[![AUR](https://repology.org/badge/version-for-repo/aur/vk-scraper.svg)](https://aur.archlinux.org/packages/vk-scraper)

vk-scraper is a command-line application written in Python that scrapes and downloads VK user's / community's data. Use responsibly.

To get a better understanding of how it works, head to [the docs](DOCS.md).

Features
--------
- Scrape photos
- Scrape videos (both uploaded and external)
- Scrape saved photos
- Scrape stories

Install
-------

#### Arch GNU/Linux
For the **stable** version ([vk-scraper](https://aur.archlinux.org/packages/vk-scraper)):

    git clone https://aur.archlinux.org/vk-scraper.git vk-scraper

For the **git** version ([vk-scraper-git](https://aur.archlinux.org/packages/vk-scraper-git)):

    git clone https://aur.archlinux.org/vk-scraper-git.git vk-scraper

Then build & install:

    cd vk-scraper 
    makepkg -sic

Or [use an AUR helper](https://wiki.archlinux.org/title/AUR_helpers) of your choice.

#### Other distros
For the **stable** version:

    $ pip3 install vk-scraper --upgrade --user

For the **git** version:

    $ pip3 install git+https://github.com/vanyasem/VK-Scraper.git --upgrade --user

Usage
-----
To scrape media:
```bash
vk-scraper <username/community> -u <your username> -p <your password>
```
*By default, downloaded media will be placed in `<current working directory>/<username>`.*

To specify multiple users/communities, pass a comma separated list of users:
```bash
vk-scraper username1,community1,username2,username3,community2
```

You can also supply a file containing a list of users/communities:
```bash
vk-scraper -f scrape_list.txt
```

```
$ cat vk_users.txt
username1
community1
username2
username3
community2
...
```
*Usernames may be separated by newlines, commas, semicolons, or whitespace.*

Arguments
---------
```
--help -h             Show help message and exit

--login-user  -u      Your VK username

--login-pass  -p      Your VK password

--filename    -f      Path to a file containing a list of users/communities to scrape

--destination -d      Specify destination folder. By default, media will
                      be downloaded to <current working directory>/<username>

--retain-username -n  Creates a subdirectory for each scraped name when the flag is set

--media-types -t      Specify media types to scrape. Enter as space separated values.
                      Valid values are image, saved, video, story, wall, or none
                      (defaults to image)

--latest              Scrape only new media since the last scrape. Uses the last modified
                      time of the latest media item in the destination directory for comparasion

--quiet       -q      Be quiet while scraping

--maximum     -m      Maximum number of items to scrape

--offset      -o      Offset from which the scrape starts. 0 is from the oldest. (Defaults to 0)
```

Contribution
------------
1. Check open issues, or open a new one to start a discussion around
   your idea or a bug you found
2. Fork the repository and make your changes
3. Send a pull request

Futurelog
---------
- Scrape by hashtag
- Scrape by location
- Save metadata to a file (likes, comments, etc)
- Sort photos by their albums
