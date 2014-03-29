from hike import app


# def recordUser(session):
# 	name = session(['name'])
# 	family_name = session(['family_name'])
# 	email = session(['email'])
# 	gender = session(['gender'])
#     return


@app.route('/user/<nickname>')
def user(nickname):
    if not session['name']:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    posts = [
        { 'author': user, 'body': 'Test post #1' },
        { 'author': user, 'body': 'Test post #2' }
    ]
    return render_template('user.html',
        user = user)