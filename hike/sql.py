#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# File: sql.py
# by BitK
# lu.k.philippe@gmail.com
#
from flask import g
import sqlite3

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
    for road_name,points in roads.iteritems():
        cursor = get_db().cursor()
        r = "INSERT INTO roads(name, points) VALUES (?, ?);"
        update_db(r, [str(road_name), str(points)])


def getRoads():
    r = ('SELECT points '
         'FROM roads LIMIT 1 ')
    row = query_db(r, one=True)
    return row[0]