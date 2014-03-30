#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# File: sql.py
# by BitK
# lu.k.philippe@gmail.com
#
from flask import g
from collections import namedtuple
import sqlite3
import json

class SQLError(Exception):
    pass

def connect_db():
    return sqlite3.connect("./hike/hike.db")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

def update_db(query, args=()):
    db = get_db()
    db.execute(query, args)
    db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def addRoad(road):
    r = "INSERT INTO roads(name, points, start, end, distance) VALUES (?, ?, ? ,?, ?);"
    update_db(r, [road["name"], json.dumps(road["tracks"]), road["start"], road["end"], road["distance"]])

def addPoi(poi):
    r = "INSERT INTO poi(name, position, type) VALUES (?, ?, ?);"
    update_db(r, [poi["title"], json.dumps(poi["position"]), int(poi["type"])])


def getRoad(road_id):
    r = ('SELECT points '
         'FROM roads '
         'WHERE id = ? '
         'LIMIT 1 ')
    row = query_db(r, [road_id], one=True)
    return row

def getRoads():
    r = ('SELECT name, points, start, end, distance '
         'FROM roads ')
    row = query_db(r)
    l = list()
    for r in row:
        road = {}
        road["name"] = r[0]
        road["points"] = json.loads(r[1]) if r[1] else ""
        road["start"] = json.loads(r[2]) if r[2] else ""
        road["end"] = json.loads(r[3]) if r[3] else ""
        road["distance"] = r[4]
        l.append(road)
    return l

def getPois():
    Pois = namedtuple("Pois", "position name picture type")
    r = ('SELECT position, name, picture, type '
         'FROM pois')
    row = query_db(r)
    pois = [Pois(*r)._asdict() for r in row]
    for p in pois:
        p["position"] = json.loads(p["position"])
    return pois

def addUser(user):
    r = ("REPLACE INTO users(name, gender, email) VALUES (?, ?, ?);")
    update_db(r, [user['name'], user['gener'], user['email']])

def getId(self):
    r = ("SELECT id FROM users WHERE id = ?;")
    uid = query_db(r, [self], one=True)
    return uid is not None

def getSeek(seek):
    r = ("SELECT name, points FROM roads WHERE name LIKE (?)")
    ns = query_db(r, ["%%%s%%" %seek["roads"]] )
    ns = [n[0] for n in ns]
    return ns
