#!/usr/bin/env python

from distutils.core import setup

setup(
    name='deepcite',
    packages=['deepcite'],
    install_requires=[
        "apipkg==1.4", "beautifulsoup4==4.6.0", "bs4==0.0.1", "execnet==1.4.1",
        "nltk==3.2.5", "numpy==1.13.3", "pep8==1.7.0", "py==1.4.34",
        "pytest==3.2.3", "pytest-cache==1.0", "pytest-pep8==1.0.6",
        "six==1.11.0"
    ])
