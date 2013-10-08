#!/usr/bin/env python
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

README = path.abspath(path.join(path.dirname(__file__), 'README.md'))
desc = 'A Python util to easily download videos from vine'

setup(
    name='vine_dwl',
    version='0.0.1',
    author='Zaurky',
    author_email='zaurky@zeb.re',
    description=desc,
    long_description=open(README).read(),
    license='GPLV2',
    url='http://github.com/zaurky/vine_dwl',
    packages=['vine_dwl'],
    scripts=['bin/vine_dwl'],
    install_requires=[
        'BeautifulSoup',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
