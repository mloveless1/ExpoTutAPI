from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.DateApp
profiles = db.profiles


@app.route('/', methods=['GET'])
def get_articles():
    return jsonify({"Hello:": "World!"})


if __name__ == '__main__':
    app.run()
