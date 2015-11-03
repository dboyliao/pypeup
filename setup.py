#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pypeup import __author__, __license__, __version__

def read(fname):
    with open(fname) as rf:
        return rf.read()

long_description = read("README.md")

if __name__ == "__main__":

    setup(name = "pypeup",
          version = '.'.join(__version__),
          author = __author__,
          author_email = 'qmalliao@gmail.com',
          long_description = long_description,
          description = 'An easy module for building data pipe in python.',
          license = __license__,
          url = "https://github.com/dboyliao/pypeup",
          keywords = 'python data pipeline',
          packages = find_packages(exclude = ['tests']),
          install_requires=["nose", "numpy", ])