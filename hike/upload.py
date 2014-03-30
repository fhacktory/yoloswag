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
import json
import backend
import math

def distance_on_unit_sphere(lat1, long1, lat2, long2):
    phi1 = math.radians(90.0 - lat1)
    phi2 = math.radians(90.0 - lat2)
    theta1 = math.radians(long1)
    theta2 = math.radians(long2)
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    return arc * 6373


def getDist(track):
    point = track[0]
    dst = 0.0
    for t in track[1:]:
        d = distance_on_unit_sphere(point[0], point[1], t[0], t[1])
        dst += d
        point = t
    return dst


@app.route("/upload", methods=["POST"])
def upload():
    js = request.form.get("json", None)
    if js is None:
        return "KO"

    road = json.loads(js)
    road["distance"] = getDist(road["tracks"])
    road["start"] = json.dumps(road["tracks"][0])
    road["end"] = json.dumps(road["tracks"][-1])
    road["elevation"] = backend.calculateElevetionDistance(road["tracks"])
    sql.addRoad(road)
    return "OK"

@app.route("/poi", methods=["POST"])
def addpoi():
    js = request.form.get("json", None)
    if js is None:
        return "KO"

    poi = json.loads(js)
    sql.addPoi(poi);
    return "OK"
