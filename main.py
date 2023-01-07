

"""
This project develops a Todolist application using python and flask as the backend framework.
This file contains all the necessary routes and controllers
"""

# Import relevant libraries 
from flask import Flask, render_template, request, flash, session, redirect, url_for, g
from model import users
from passlib.hash import sha256_crypt
import uuid

# Generate random string
lowercase_str = uuid.uuid4().hex 

insights = Flask(__name__)

# Secret key to manage sessions
insights.secret_key = lowercase_str 

"""
All individual routes and pages that will exist are below:
"""

# Homepage
@insights.route('/', methods = ['GET'])
def homepage():
    if 'username' in session:
        g.user = session['username']
        return redirect(url_for('dashboard',message=g.user))

    return render_template('index.html')

# Dashboard
@insights.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    userid = users.get_user_id(session['username'])
    return render_template('dashboard.html',message=session['username'])

# Signing up
@insights.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method== 'GET':
        return render_template('signup.html')
    else:
        username = request.form['user']
        email = request.form['email']
        password = request.form['pass1']
        message = message= users.signup(username, email, password)
        if message=='true':
            flash("Signup successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Username already exists", "danger")
            return render_template('signup.html')

# Logging in
@insights.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('username', None)
        areyouuser = request.form['user']
        has_pass = users.check_pasword(areyouuser)

        # no password for such username or incorrect password (in this case, the hashed password not from the same source)
        if (has_pass=='false') or not(sha256_crypt.verify(request.form['pass'], has_pass)):
            flash("Login credentials incorrect", "danger")
            return render_template('login.html')

        if (sha256_crypt.verify(request.form['pass'], has_pass)):
            session['username'] = request.form['user']
            flash("Login successful. Welcome!", "success")
            return redirect(url_for('dashboard'))

    return render_template('login.html')

# Logout
@insights.route('/logout')
def logout():
    session.pop('username', None)
    flash("You're successfully logged out","success")
    return redirect(url_for('homepage'))

if __name__ =='__main__':
    insights.run(port=7000,debug=True)
