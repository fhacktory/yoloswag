from hike import app

@app.route('/user/<idUser:int>')
def user_profile(idUser = 0):
    if idUser == 0
        abort(404)
    return render_template("index.html", view="profile.html")


 