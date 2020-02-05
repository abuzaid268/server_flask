from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/sanity")
def foo():
    print("got request")
    return json.dumps({'hello': 'its me'})


@app.route("/home")
def bar():
    print("got request")
    return json.dumps("Home")


@app.route('/users/<id>')
def get_user(id):
    return json.dumps(users[id])


users = {
    "123": {"name": "bubu"},
    "124": {"name": "kuku"}
}


@app.route("/users")
def get_users():
    start = request.args.get("start")
    users_with_b = [users[s] for s in users if users[s]["name"].startswith(start)]
    return json.dumps(users_with_b)


if __name__ == '__main__':
    app.run(port=3000)
