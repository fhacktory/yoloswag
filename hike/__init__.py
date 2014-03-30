#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# File: __init__.py
# by BitK
# lu.k.philippe@gmail.com
#

from flask import Flask

app = Flask(__name__)

from hike import main, oaGooglePlus, profile , upload, sql, search

