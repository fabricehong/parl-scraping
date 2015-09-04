# -*- coding: UTF8 -*-
'''
Parlement files scraper
~~~~~~~~~~~~~~~~~~~~~~~

Control the Bactosense Flowcytometer.

'''

from setuptools import setup

setup(
    name='Swiss Parlement Scraper',
    description="Scrape and analyze transcriptions of swiss parlement sessions.",
    version='0.1dev',
    author='OpenData.ch'
    author_email=''
    packages=['scraper', 'analyze', ],
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
        'sqlalchemy'
    ],
)
