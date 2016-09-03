#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://rohitja.in'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/.travis.yml']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},'extra/.travis.yml': {'path': '.travis.yml'}, }

# Following items are often useful when publishing

DISQUS_SITENAME = "rohitjain-1"
GOOGLE_ANALYTICS = "UA-46114608-2"