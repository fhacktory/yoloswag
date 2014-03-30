
# #!/usr/bin/python2
# # -*- coding: utf-8 -*-
# #
# # File: upload.py
# # by BitK
# # lu.k.philippe@gmail.com
# #
# from hike import app
# from hike import sql
# from pykml import parser
# from flask import request, abort
# #import pykml
# from lxml.etree import XMLSyntaxError
# import json

# @app.route("/upload", methods=["POST"])
# def upload():
#     road = {}
#     js = request.form.get("json", None)
#     if js is None:
#         return "KO"
    
#     sql.addRoad(json.loads(js))
#     return "OK"
