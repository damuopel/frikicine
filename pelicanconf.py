#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David'
SITENAME = 'Frikicine'
SITEURL = ''
DESCRIPTION = 'Blog sobre noticias relacionadas con el mundo friki en el cine'
FAVICON = '/img/Logo.png'
LOGO = '/img/Logo.png'
SITESUBTITLE = 'Blog sobre noticias del mundo friki en el cine'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'themes/pelican-mg'

PLUGIN_PATHS = ["plugins"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['paginas','img']
ARTICLE_PATHS = ['articulos',]
ARTICLE_URL = 'articulos/{slug}.html'
ARTICLE_SAVE_AS = 'articulos/{slug}.html'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

FOOTER = 'Made with &hearts;'