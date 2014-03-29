from hike import app

@app.route("/")
def mainindex():
    return "Helloworld"
