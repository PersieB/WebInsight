"""
This project develops a Todolist application using python and flask as the backend framework.
This file contains all the necessary routes and controllers
"""

# Import relevant libraries 
from flask import Flask, render_template, request, flash, session, redirect, url_for, g
#from data_models import user_model, todo_model, task_model
from passlib.hash import sha256_crypt
import uuid

# Generate random string
lowercase_str = uuid.uuid4().hex 


todo_app = Flask(__name__)

# Secret key to manage sessions
todo_app.secret_key = lowercase_str 


"""
All individual routes and pages that will exist are below:
"""

# Homepage
@todo_app.route('/', methods = ['GET'])
def homepage():
    return render_template('login.html')

# Signing up
@todo_app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template('signup.html')
    '''
    if request.method== 'GET':
        return render_template('signup.html')
    else:
        username = request.form['user']
        email = request.form['email']
        password = request.form['pass1']
        message = message= user_model.signup(username, email, password)
        if message=='true':
            flash("Signup successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Username already exists", "danger")
            return render_template('signup.html')'''


# Logging in
@todo_app.route('/login', methods = ['GET', 'POST'])
def login():
    '''
    if request.method=='POST':
        session.pop('username', None)
        areyouuser = request.form['user']
        has_pass = user_model.check_pasword(areyouuser)

        # no password for such username or incorrect password (in this case, the hashed password not from the same source)
        if (has_pass=='false') or not(sha256_crypt.verify(request.form['pass'], has_pass)):
            flash("Login credentials incorrect", "danger")
            return render_template('login.html')

        if (sha256_crypt.verify(request.form['pass'], has_pass)):
            session['username'] = request.form['user']
            flash("Login successful. Welcome!", "success")
            return redirect(url_for('dashboard'))'''

    return render_template('login.html')

'''
# About page
@todo_app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')


# Privacy page
@todo_app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')


# Terms of use page
@todo_app.route('/terms', methods = ['GET'])
def terms():
    return render_template('terms.html')


# Dashboard
@todo_app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    userid = user_model.get_user_id(session['username'])
    todolists = todo_model.show_todos(userid)
    return render_template('dashboard.html',message=session['username'], todos = todolists)


# Signing up
@todo_app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method== 'GET':
        return render_template('signup.html')
    else:
        username = request.form['user']
        email = request.form['email']
        password = request.form['pass1']
        message = message= user_model.signup(username, email, password)
        if message=='true':
            flash("Signup successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Username already exists", "danger")
            return render_template('signup.html')


# Logging in
@todo_app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('username', None)
        areyouuser = request.form['user']
        has_pass = user_model.check_pasword(areyouuser)

        # no password for such username or incorrect password (in this case, the hashed password not from the same source)
        if (has_pass=='false') or not(sha256_crypt.verify(request.form['pass'], has_pass)):
            flash("Login credentials incorrect", "danger")
            return render_template('login.html')

        if (sha256_crypt.verify(request.form['pass'], has_pass)):
            session['username'] = request.form['user']
            flash("Login successful. Welcome!", "success")
            return redirect(url_for('dashboard'))

    return render_template('login.html')


# Display tasks
@todo_app.route('/tasks', methods = ['GET', 'POST'])
def tasks():
    return render_template('tasks.html',message=session['username'])


# Logout
@todo_app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You're successfully logged out","success")
    return redirect(url_for('homepage'))


# Add todo list 
@todo_app.route('/todo', methods = ['GET', 'POST'])
def todo():
    if request.method=='GET':
        return render_template('addtodos.html')
    else:
        userid = user_model.get_user_id(session['username'])
        title = request.form['title']
        todo_model.add_todo(title, userid)
        flash("Successfully added Todo item. Click to add associated tasks","success")
        return redirect(url_for('dashboard'))


# Update todo title
@todo_app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update_todo(id):
    todo_id = id
    if request.method=='GET':
        return render_template('edittodos.html')
    else:
        title = request.form['title']
        todo_model.update_todo(title,todo_id)
        flash("Todo item successfully updated.","success")
        return redirect(url_for('dashboard'))


# Delete todo item and its tasks
@todo_app.route('/delete/<int:id>')
def delete_todo(id):
    task_model.delete_alltodo_tasks(id)
    todo_model.delete_todo(id)
    flash("Todo list successfully deleted.","success")
    return redirect(url_for('dashboard'))


# Display tasks based on todo item clicked
@todo_app.route('/showtask/<int:todo_id>', methods = ['GET', 'POST'])
def todo_tasks(todo_id):
    activities = task_model.show_task(todo_id)
    todo = todo_model.select_one(todo_id)
    return render_template('tasks.html',message=session['username'], tasks = activities, title = todo[1], todo_id=todo_id)


# Add a new task under a todo item
@todo_app.route('/task/<int:todo_id>', methods = ['GET', 'POST'])
def task(todo_id):
    if request.method=='GET':
        return render_template('addtask.html',todo_id=todo_id)
    else:
        activity = request.form['activity']
        task_model.add_task(todo_id, activity)
        flash("Successfully added Todo. Click to add task","success")
        return redirect(url_for('todo_tasks',todo_id=todo_id))


# Update task activity name
@todo_app.route('/updatetask/<int:id>', methods = ['GET', 'POST'])
def update_task(id):
    todoid = task_model.select_todo_in_tasks(id)
    if request.method=='GET':
        return render_template('edittask.html',todo_id=todoid)
    else:
        activity = request.form['activity']
        task_model.update_activityname(activity,id)
        flash("Activity name successfully updated.","success")
        return redirect(url_for('todo_tasks',todo_id=todoid))


# Check of task status as NOT STARTED, IN-PROGRESS OR COMPLETED
@todo_app.route('/updatestat/<int:id>/<string:status>')
def update_status(id, status):
    task_model.update_status(status,id)
    todoid = task_model.select_todo_in_tasks(id)
    all_task_statuses = task_model.all_todo_task_statuses(todoid)
    print(all_task_statuses)
    todo_status = todo_model.check_progress(all_task_statuses)
    print(todo_status)
    todo_model.update_todo_status(todo_status,todoid)
    flash("Status successfully updated.","success")
    return redirect(url_for('todo_tasks',todo_id=todoid))


# Delete task
@todo_app.route('/deletetask/<int:id>')
def delete_task(id):
    todoid = task_model.select_todo_in_tasks(id)
    task_model.delete_task(id)
    flash("Activity successfully deleted.","success")
    return redirect(url_for('todo_tasks',todo_id=todoid))
'''

if __name__ =='__main__':
    todo_app.run(port=7000,debug=True)