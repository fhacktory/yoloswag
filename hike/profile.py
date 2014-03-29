from hike import app
from flask import abort, render_template


@app.route('/user/<idUser:int>')
def user_profile(idUser = 0):
    if idUser == 0:
        abort(404)
    return render_template("index.html", view="profile.html")


 