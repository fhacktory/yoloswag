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


def addRoads(roads):
    for road_name,track in roads.iteritems():
        cursor = get_db().cursor()
        r = "INSERT INTO roads(name, points) VALUES (?, ?);"
        update_db(r, [str(road_name), str(track)])


def getRoad(road_id):
    r = ('SELECT points '
         'FROM roads '
         'WHERE id = ? '
         'LIMIT 1 ')
    row = query_db(r, [road_id], one=True)
    return row[0]

def getRoads():
    r = ('SELECT points '
         'FROM roads ')
    row = query_db(r)
    return [json.loads(r[0]) for r in row]

def getAllPois():
    Pois = namedtuple("Pois", "position name picture type")
    r = ('SELECT position, name, picture, type '
         'FROM pois')
    row = query_db(r)
    pois = [Pois(*r)._asdict() for r in row]
    for p in pois:
        p["position"] = json.loads(p["position"])
    return pois


def getPois(road_id):
    Pois = namedtuple("Pois", "position name picture type")
    r = ('SELECT position, name, picture, type '
         'FROM pois WHERE road_id = ?')
    row = query_db(r, [road_id])
    pois = [Pois(*r)._asdict() for r in row]
    for p in pois:
        p["position"] = json.loads(p["position"])
    return pois

def addUser(user):
    r = "INSERT INTO user(name, gender, email) VALUES (?, ?, ?,);"
    update_db(r, [user['name'], user['gener'], user['email'])
