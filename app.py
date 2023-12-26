import json
from flask import Flask, render_template, request, make_response, redirect, jsonify
from flask_cors import CORS
from ToDoList.main import retrieve_tasks, add_tasks, remove_tasks, complete_tasks
from ToDoList.UserCheck import check_user
from ToDoList.UserRegistration import add_user
from ToDoList.UserLogin import check_credentials

app = Flask(__name__)
CORS(app, resources={r"/todo/*": {"origins": "*"}})


@app.route('/')
def root():
    if 'logged_in' in request.cookies and request.cookies.get('logged_in') == "yes":
        return redirect("/todo", code=302)
    else:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('logged_in', 'no', max_age=28480)
        return resp


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if check_credentials(username, password):
        print(f"Received login request. Username: {username}")
        resp = redirect("/todo", code=302)
        resp.set_cookie('username', username, max_age=28480)
        resp.set_cookie('logged_in', 'yes', max_age=28480)
        return resp
    else:
        print(f"Received incorrect login request. Username: {username}")
        return "incorrect password"


@app.route('/register', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')

    if not check_user(username):
        add_user(username, password)
        resp = redirect("/todo", code=302)
        resp.set_cookie('username', username, max_age=28480)
        resp.set_cookie('logged_in', 'yes', max_age=28480)
        return resp
    else:
        return f"Username {username} already exists"


@app.route('/todo', methods=['POST', 'GET'])
def todo():
    username = request.cookies.get('username')
    data = {
        "username": username
    }
    tasks = retrieve_tasks(username)
    print(tasks)
    return render_template("todo.html", data=data, task=tasks)


@app.route('/todo/add/<task>', methods=['POST'])
def add_task(task):
    try:
        username = request.cookies.get('username')
        data = request.get_json()
        add_tasks(username, data['task'])
        return jsonify({'status': 'success'})

    except Exception as e:
        print(f"Error processing POST request: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/todo/remove/<task>', methods=['POST'])
def remove_task(task):
    try:
        username = request.cookies.get('username')
        data = task
        remove_tasks(username, data)
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"Error processing POST request: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/todo/complete/<task>', methods=['POST'])
def complete_task(task):
    try:
        username = request.cookies.get('username')
        data = task
        complete_tasks(username, data)
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"Error processing POST request: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/logout')
def logout():
    resp = make_response(redirect('/', code=302))
    resp.delete_cookie('username')
    resp.delete_cookie('logged_in')
    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')