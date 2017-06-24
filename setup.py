from setuptools import setup, find_packages

setup(
    name='VK-Scraper',
    version='1.0.0.dev1',
    description='',
    url='https://github.com/vanyasem/VK-Scraper',
    author='Ivan Semkin',
    author_email='ivan@semkin.ru',
    license='GPL-2.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent'
        'Programming Language :: Python'
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    install_requires=['vk_api'],
    entry_points={
        'console_scripts': [
            'vk-scraper=vk_scraper.app:main',
        ],
    },
    keywords=['vk', 'vkontakte', 'scraper', 'download', 'media', 'photos', 'videos', 'stories']
)
