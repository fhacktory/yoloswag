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
import pykml
from lxml.etree import XMLSyntaxError


@app.route("/upload", methods=["POST"])
def upload():
    road = {}
    road["username"] = request.form.get("username", None)
    road["kml"] = open("/home/philip_l/fhacktory/repo/hike/kml").read()#request.form.get("kml", None)

    try:
        kml = parser.fromstring(road["kml"])
    except XMLSyntaxError as e:
        abort(400)
    points = {}
    for placemark in kml.Document.Placemark:
        if hasattr(placemark, "LineString"):
            points[placemark.name] = [[float(x) for x in c.split(",")] for c in placemark.LineString.coordinates.text.split()]
    sql.addRoads(points)
    return(str(points))
    
