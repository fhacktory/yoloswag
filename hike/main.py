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

<<<<<<< HEAD
@app.route("/")
def home():
	return render_template("index.html")
=======
@app.route('/')
def index():
    if 'email' not in session:
    	return render_template("index.html", view="home.html")
    else:
    	return render_template("index.html", view="welcome.html", session=session)
>>>>>>> dev

@app.route("/map")
def test():
    pois = json.dumps(sql.getPois(1))
<<<<<<< HEAD
    return render_template("map.html", track=sql.getRoad(1), POIs=pois)
# <div id="map-canvas"/>
=======
    return render_template("index.html", tracks=sql.getRoads(), POIs=pois, view="home.html")
>>>>>>> dev
