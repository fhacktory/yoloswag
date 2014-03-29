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

@app.route('/')
def index():
    if 'email' not in session:
    	return render_template("index.html", view="home.html")
    else:
    	return render_template("index.html", view="welcome.html", session=session)

@app.route("/test")
def test():
    pois = json.dumps(sql.getAllPois())
    return render_template("index.html", tracks=sql.getRoads(), POIs=pois)
