#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# File: upload.py
# by BitK
# lu.k.philippe@gmail.com
#
from hike import app
from hike import sql
from pykml import parser
from flask import request, abort
#import pykml
from lxml.etree import XMLSyntaxError
import json

@app.route("/upload", methods=["POST"])
def upload():
    road = {}
    road["username"] = request.form.get("username", None)
    road["kml"] = open("./hike/GR20.kml").read()#request.form.get("kml", None)

    try:
        kml = parser.fromstring(road["kml"])
    except XMLSyntaxError as e:
        abort(400)
    track = {}
    for placemark in kml.Document.Placemark:
        if hasattr(placemark, "LineString"):
            pois = [[float(x) for x in c.split(",")] for c in placemark.LineString.coordinates.text.split()]
            pois = [[p[1], p[0], p[2]] for p in pois]
            track[placemark.name] = json.dumps(pois)
    sql.addRoads(track)
    return(str(track))
