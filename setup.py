#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pypipe import __author__, __license__, __version__

def read(fname):
    with open(fname) as rf:
        return ''.join(rf.readlines())

if __name__ == "__main__":

    setup(name = "pypipe",
          version = '.'.join(__version__),
          author = __author__,
          author_email = 'qmalliao@gmail.com',
          long_description = read('README.md'),
          description = 'An easy module for building data pipe in python.',
          license = __license__,
          url = "https://github.com/dboyliao/pypipe",
          keywords = 'python pipe',
          packages = find_packages(exclude = ['tests']))