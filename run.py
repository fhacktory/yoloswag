#!/usr/bin/python2

import os
from hike import app


app.secret_key = os.urandom(32)
app.run(debug=True, host="127.0.0.1", port=1337)
