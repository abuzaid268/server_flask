from flask import Flask, request, Response
import json
import requests

app = Flask(__name__, static_url_path='', static_folder='dist')
log = []
data = {
    "8112": {
        "title": "Name of the Wind",
        "author": "Patrick Rothfuss"
    },
    "9121": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger"
    },
    "1081": {
        "title": "The Giver",
        "author": "Lois Lowry"
    }
}
store = [
    { "name": "table", "inventory": 3, "price": 800 },
    { "name": "chair", "inventory": 16, "price": 120 },
    { "name": "couch", "inventory": 1, "price": 1200 },
    { "name": "picture frame", "inventory": 31, "price": 70 }
]

@app.route("/sanity")
def foo():
    print("got request")
    return json.dumps("Server is up and running smoothly")


@app.route("/home")
def bar():
    print("got request")
    return json.dumps("Home")


@app.route('/users/<id>')
def get_user(id):
    return json.dumps(users[id])


@app.route('/life')
def set_life():
    return "42"


@app.route('/landing/<username>')
def greetuser(username):
    return Response("Hi there {}".format(username))


users = {
    "tilda": "You've done a wonderful job",
    "jeremy": "You need to improve your form, but good perseverance",
    "Marta": "You're incredible"
}


@app.route("/user/<usersID>")
def get_users(usersID):
    start = request.args.get(usersID)
    users_with_b = [users[s] for s in users if s == usersID]
    return json.dumps(users_with_b)


@app.route('/optionalParameters')
def query_params():
    json_string = json.dumps(request.args)
    return Response(json_string)


@app.route('/details')
def query_city():
    json_string = json.dumps(request.args)
    log.append(json_string)
    return Response(json_string)


@app.route('/print')
def print_log():
    return json.dumps(log)


@app.route('/books')
def get_book():
    json_string = json.dumps(request.args)
    return Response(json_string)


@app.route('/<path:file_path>')
def serve_static_file(file_path):
    return app.send_static_file(file_path)


@app.route('/priceCheck/<furname>')
def price_check(furname):
    json_string = request.args.get(furname)

    return json.dumps()


if __name__ == '__main__':
    app.run(port=3000)
    books_url = 'http://localhost:3000/books/{}'.format(id)
    res = requests.get(url=books_url)
    print(res.json())