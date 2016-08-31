#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rohit Jain'
SITENAME = 'Arbit Musings'
SITEURL = 'http://rohitja.in'
SITELOGO = 'https://graph.facebook.com/738607928/picture?type=large'

PATH = 'content'
ROBOTS = 'index, follow'
TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('about', '#'),
         ('contact', '#'),
         ('photolog', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/esawtooth'),
          ('facebook', 'http://www.facebook.com/rohit7jain'),
	  ('soundcloud', 'https://soundcloud.com/esawtooth'),
	  ('envelope-o', 'mailto://mail@rohitja.in'),
	  ('linkedin','https://www.linkedin.com/in/rohit7jain'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
