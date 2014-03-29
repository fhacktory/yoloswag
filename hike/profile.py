from hike import app, sql
from flask import abort, render_template
import sqlite3



@app.route('/user/<int:idUser>')
def user_profile(idUser = 0):
	if sql.getId(idUser):
		return render_template("index.html", view="profile.html")

 