from flask import Flask, jsonify
from routes import users_bp
from routes import profiles_bp
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

app.register_blueprint(users_bp)
app.register_blueprint(profiles_bp)


@app.route('/', methods=['GET'])
def get_articles():
    return jsonify({"Hello:": "World!"})


if __name__ == '__main__':
    app.run()
