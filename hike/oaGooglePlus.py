from flask import request, session, redirect, url_for
from hike import app
import urllib
import requests

# app.secret_key = 'iwonttellyou'

redirect_uri = 'http://127.0.0.1:1337/login/google/auth'
client_id = '876045027884-ttf6o8eppj60soeppordc3nkko4h09fg.apps.googleusercontent.com'  # get from https://code.google.com/apis/console
client_secret = 'lcz3HMPx_QMDz2LNzbpcVHFy'

auth_uri = 'https://accounts.google.com/o/oauth2/auth'
token_uri = 'https://accounts.google.com/o/oauth2/token'
scope = ('https://www.googleapis.com/auth/userinfo.profile',
   'https://www.googleapis.com/auth/userinfo.email')
profile_uri = 'https://www.googleapis.com/oauth2/v1/userinfo'


@app.route('/logout')
def logout():
    session.pop('email', '')
    session.pop('name', '')
    session.pop('family_name', '')
    session.pop('gener', '')
    return redirect(url_for('index'))


@app.route('/login')
def login():
# Step 1
    params = dict(response_type='code',
        scope=' '.join(scope),
        client_id=client_id,
        approval_prompt='force',  # or 'auto'
        redirect_uri=redirect_uri)
    url = auth_uri + '?' + urllib.urlencode(params)
    return redirect(url)


@app.route('/login/google/auth')
def callback():
    if 'code' in request.args:
        # Step 2
        code = request.args.get('code')
        data = dict(code=code,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            grant_type='authorization_code')
        r = requests.post(token_uri, data=data)
        # Step 3
        access_token = r.json()['access_token']
        r = requests.get(profile_uri, params={'access_token': access_token})
        session['email'] = r.json()['email']
        session['name'] = r.json()['name']
        session['family_name'] = r.json()['family_name']
        session['gener'] = r.json()['gender']
        return redirect(url_for('index'))
    else:
        return 'ERROR'