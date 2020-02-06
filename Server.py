# from flask import Flask, request, Response
# import json
# import requests
#
# app = Flask(__name__, static_url_path='', static_folder='dist')
# log = []
# data = {
#     "8112": {
#         "title": "Name of the Wind",
#         "author": "Patrick Rothfuss"
#     },
#     "9121": {
#         "title": "The Catcher in the Rye",
#         "author": "J.D. Salinger"
#     },
#     "1081": {
#         "title": "The Giver",
#         "author": "Lois Lowry"
#     }
# }
# store = [
#     { "name": "table", "inventory": 3, "price": 800 },
#     { "name": "chair", "inventory": 16, "price": 120 },
#     { "name": "couch", "inventory": 1, "price": 1200 },
#     { "name": "picture frame", "inventory": 31, "price": 70 }
# ]
#
# @app.route("/sanity")
# def foo():
#     print("got request")
#     return json.dumps("Server is up and running smoothly")
#
#
# @app.route("/home")
# def bar():
#     print("got request")
#     return json.dumps("Home")
#
#
# @app.route('/users/<id>')
# def get_user(id):
#     return json.dumps(users[id])
#
#
# @app.route('/life')
# def set_life():
#     return "42"
#
#
# @app.route('/landing/<username>')
# def greetuser(username):
#     return Response("Hi there {}".format(username))
#
#
# users = {
#     "tilda": "You've done a wonderful job",
#     "jeremy": "You need to improve your form, but good perseverance",
#     "Marta": "You're incredible"
# }
#
#
# @app.route("/user/<usersID>")
# def get_users(usersID):
#     start = request.args.get(usersID)
#     users_with_b = [users[s] for s in users if s == usersID]
#     return json.dumps(users_with_b)
#
#
# @app.route('/optionalParameters')
# def query_params():
#     json_string = json.dumps(request.args)
#     return Response(json_string)
#
#
# @app.route('/details')
# def query_city():
#     json_string = json.dumps(request.args)
#     log.append(json_string)
#     return Response(json_string)
#
#
# @app.route('/print')
# def print_log():
#     return json.dumps(log)
#
#
# @app.route('/books')
# def get_book():
#     json_string = json.dumps(request.args)
#     return Response(json_string)
#
#
# @app.route('/<path:file_path>')
# def serve_static_file(file_path):
#     return app.send_static_file(file_path)
#
#
# @app.route('/priceCheck/<furname>')
# def price_check(furname):
#     json_string = request.args.get(furname)
#
#     return json.dumps()
#
#
# if __name__ == '__main__':
#     app.run(port=3000)
#     books_url = 'http://localhost:3000/books/{}'.format(id)
#     res = requests.get(url=books_url)
#     print(res.json())

from flask import Flask, Response, request
import json
import requests
from copy import deepcopy

app = Flask(__name__, static_url_path='', static_folder='dist')

users = [
    {"name": "Mohammad", "Age": "23.5", 'Number': '0546687575'},
    {"name": "Wasseem", "Age": "26.5", 'Number': '0545534758'},
    {"name": "Sami", "Age": "25.5", 'Number': '0542076838'},
    {"name": "Yazan", "Age": "23.5", 'Number': '0527043393'}
]

store = [
    {"name": "table", "inventory": 3, "price": 800},
    {"name": "chair", "inventory": 16, "price": 120},
    {"name": "couch", "inventory": 1, "price": 1200},
    {"name": "picture frame", "inventory": 31, "price": 70}
]


@app.route('/')
def home_page():
    return json.dumps("Welcome to my homepage")


@app.route('/secondery/<userid>')
def print_users(userid):
    user_info = [users[i] for i in range(len(users)) if users[i]["name"] == userid]
    return json.dumps(user_info)


@app.route('/<path:filepath>')
def open_image(filepath):
    return app.send_static_file(filepath)


@app.route('/priceCheck/<name>')
def get_price(name):
    price = [store[i]["price"] for i in range(len(store)) if store[i]["name"] == name]
    if price:
        price = {'price': str(price).strip('[]')}
    else:
        price = {"price": 'NULL'}
    return json.dumps(price)


@app.route('/buy/<name>')
def buy_item(name):
    item = {}
    for dict in store:
        if dict["name"] == name:
            if dict["inventory"] > 0:
                dict["inventory"] -= 1
                item = dict
    if item:
        return json.dumps(
            f"Congratulations, you've just bought {item['name']} for {item['price']}. There are {item['inventory']} left now in the store.")
    else:
        return "No such item"


@app.route('/sale')
def sale_item():
    store_copy = deepcopy(store)
    json_string = json.dumps(request.args.get('admin'))
    if json_string == '"true"':
        for items in store_copy:
            if items["price"] > 10:
                items["price"] //= 2
    return json.dumps(store_copy)


@app.route('/sanity')
def ret_msg():
    return "Server is up and running smoothly"


if __name__ == '__main__':
    app.run(debug=True, port=3000)
    fur_name = input("enter fur")
    url = 'localhost:3000/priceCheck/{}'.format(fur_name)
    res = requests.get(url=url)
    print(res.json())
