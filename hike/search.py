from hike import app, sql
from flask import request

@app.route('/search', methods=['POST'])
def fullSearch():
	seek = {}
	seek["roads"] = request.form.get("Search", None)
	seek["lvl"] = request.form.get('lvl', None)
	# seek["closest"] = request.get("closest", None)
	lseek = sql.getSeek(seek)
	return str(lseek)
