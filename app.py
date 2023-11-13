from flask import Flask, jsonify
from routes import users_bp
from routes import profiles_bp
from routes import messages_bp
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

app.register_blueprint(users_bp)
app.register_blueprint(profiles_bp)
app.register_blueprint(messages_bp)


@app.route('/', methods=['GET'])
def get_articles():
    return jsonify({"Hello:": "World!"})


if __name__ == '__main__':
    socketio.run(app)
