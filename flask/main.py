import flask
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("main_page.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(flask.request.form)
        login = flask.request.form["username"]
        password = flask.request.form["password"]
        print(login, password)
        return "gg wp"
    elif request.method == 'GET':
        return flask.render_template("login_page.html")


if __name__ == "__main__":
    app.run()