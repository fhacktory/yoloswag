import json
import requests
import sql

from hike import app

API_KEY = "AIzaSyBmjJxc44nSySOq2L1oan1jEmJkl4pc7i4"

@app.route('/elevation/<int:route>')
def calculateElevetionDistance(route):
    route = sql.getRoad(route)
    locations = []
    for point in route:
        print point
        point = json.loads(point)
        locations.append("{},{}".format(point[0], point[1]))
    req = "https://maps.googleapis.com/maps/api/elevation/json?key={}&sensor=true&locations='{}'".format(API_KEY, '|'.join(locations))
    print req
    rep = requests.get(req)
    print rep
    return ""
#calculateElevetionDistance()
