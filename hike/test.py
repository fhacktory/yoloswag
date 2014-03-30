#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# File: test.py
# by BitK
# lu.k.philippe@gmail.com
#

from pykml import parser


kml = parser.fromstring(open("kml").read())

print hasattr(kml.Document.Placemark[0], "Point")
