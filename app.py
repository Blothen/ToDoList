from flask import Flask, render_template, request, make_response, redirect
from ToDoList.main import add_user, get_user, __todo, check_user

app = Flask(__name__)


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
    if check_user(username):
        print(f"Received login request. Username: {username}, Password: {password}")
        resp = redirect("/todo", code=302)
        resp.set_cookie('username', username, max_age=28480)
        resp.set_cookie('logged_in', 'yes', max_age=28480)
        return resp
    else:
        print(f"Received incorrect login request. Username: {username}, Password: {password}")
        return "incorrect password"


@app.route('/register', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')

    if not check_user(username):
        add_user(username, password)
        print(f"Received signup request. Username: {username}, Password: {password}")
        resp = redirect("/todo", code=302)
        resp.set_cookie('username', username, max_age=28480)
        resp.set_cookie('logged_in', 'yes', max_age=28480)
        return resp
    else:
        return f"Username {username} already exists"


@app.route('/todo', methods=['POST', 'GET'])
def todo():
    username = request.cookies.get('username')
    data={
        'username': username
    }
    return render_template("todo.html", data=data)


@app.route('/logout')
def logout():
    resp = make_response(redirect('/', code=302))
    resp.delete_cookie('username')
    resp.delete_cookie('logged_in')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
