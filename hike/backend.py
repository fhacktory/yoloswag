import json
import requests
import sql
import gpolyencode

from hike import app

API_KEY = "AIzaSyBmjJxc44nSySOq2L1oan1jEmJkl4pc7i4"

@app.route('/elevation/<int:route>')
def calculateElevetionDistance(route):
    route = json.loads(sql.getRoad(route))
    locations = []
    while len(route) > 256:
        route = route[::2]
    encoder = gpolyencode.GPolyEncoder()
    points = encoder.encode(route)["points"]
    req = "https://maps.googleapis.com/maps/api/elevation/json?key={}&sensor=true&locations=enc:{}".format(API_KEY, points)
    rep = requests.get(req)
    print rep
    points = rep.json()["results"]
    elevation = 0
    lastelevation = points[0]["elevation"]
    for point in points[1:]:
        print point
        if point["elevation"] > lastelevation:
            print point["elevation"]
            elevation += point["elevation"] - lastelevation
        lastelevation = point["elevation"]
    return str(elevation)
