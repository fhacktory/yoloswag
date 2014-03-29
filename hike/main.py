from hike import app
from flask import g, render_template
import sql

@app.before_request
def before_request():
    g.db = sql.connect_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def mainindex():
    return "Helloworld"

@app.route("/test")
def test():
    return render_template("index.html", points=sql.getRoads())
