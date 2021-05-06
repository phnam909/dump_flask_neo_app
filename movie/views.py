from flask import Flask ,render_template,request, flash, session, redirect, url_for

from .models import User
app = Flask(__name__)
app.secret_key = "abc"

@app.route('/')
def index():
    movies = User.get_all_movie()
    print(movies)
    return render_template('index.html', movies=movies)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        user = User(username)

        if not user.register(password):
            flash('A user is already exists')
            return redirect(url_for('index'))
        else:
            flash('Register successfully')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username).verify_password(password)
        if not user:
            flash('Invalid login.')
            print(user)
        else:
            session['username'] = username
            flash('Logged in.')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/add_movie', methods=['POST'])
def add_movie():
    title = request.form['title']
    tags = request.form['tag']
    text = request.form['text']
    # if not title:
    #     flash('You must give your post a title.')
    # elif not tags:
    #     flash('You must give your post at least one tag.')
    # elif not text:
    #     flash('You must give your post a text body.')
    # else:
    #     User(session['username']).add_post(title, tags, text)
    User(session['username']).add_movie(title,tags,text)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    flash('Logged out')
    return redirect(url_for('index'))


