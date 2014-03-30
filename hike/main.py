from flask import request, session, redirect, url_for, render_template
from hike import app
from flask import g, render_template
import sql
import json

@app.before_request
def before_request():
    g.db = sql.connect_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/test')
def index():
    if 'email' not in session:
    	return render_template("index.html", view="home.html")
    else:
    	return render_template("index.html", view="welcome.html", session=session)

@app.route("/map")
def test():
    pois = json.dumps(sql.getPois(1))
    roads = json.dumps(sql.getRoads())
    return render_template("index.html", tracks=roads, POIs=pois, view="home.html")
