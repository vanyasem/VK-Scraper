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

from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'vk_api',
    'requests>=1.0.4',
    'tqdm>=3.8.0',
    'youtube_dl',
]

setup(
    name='VK-Scraper',
    version='2.0.3',
    description="Scrapes VK user's photos",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vanyasem/VK-Scraper',
    download_url='https://github.com/vanyasem/VK-Scraper/archive/v2.0.3.tar.gz',
    author='Ivan Semkin',
    author_email='ivan@semkin.ru',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'vk-scraper=vk_scraper.app:main',
        ],
    },
    keywords=['vk', 'vkontakte', 'scraper', 'download', 'media', 'photos', 'videos', 'stories']
)
