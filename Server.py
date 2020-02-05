from flask import Flask
import json

app = Flask(__name__)


@app.route("/sanity")
def foo():
    print("got request")
    return json.dumps({'hello' : 'its me'})


if __name__ == '__main__':
    app.run(port=3000)
