from flask import request, session, redirect, url_for, render_template
from hike import app

@app.route('/')
def index():
    if 'email' not in session:
    	return render_template("index.html", view="home.html")
    else:
    	return render_template("index.html", view="welcome.html", session=session)
