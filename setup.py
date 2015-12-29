# -*- coding: UTF8 -*-
'''
Parliament files scraper
~~~~~~~~~~~~~~~~~~~~~~~

OpenData Hackathon.

'''

from setuptools import setup

setup(
    name='Swiss Parliament Scraper',
    description="Scrape and analyze transcriptions of swiss parliament sessions.",
    version='0.1dev',
    author='OpenData.ch',
    author_email='',
    packages=['parl_scraper',],
    # package_data={
    #     '...': ['...', ],
    # },
    data_files=[
        # ('/etc/udev/rules.d/', ['scripts/99-usbftdi.rules']),
    ],
    entry_points={
        'console_scripts': [
            # 'target = package:function',
        ],
    },
    scripts=[
        # 'scripts/...',
    ],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'requests',
    ],
)
