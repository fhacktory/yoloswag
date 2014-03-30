from hike import app, sql
from flask import abort, render_template
import sqlite3

@app.route('/user/')
def user_profile():
	return render_template("map.html", view="profile.html")

 