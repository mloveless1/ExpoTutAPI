from flask import Blueprint, jsonify, request
from models import User
from database import database as db

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def fetch_users():
    users = db.get_all_users()
    return jsonify(users)


@users_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = db.create_user(data)
    return jsonify(new_user), 201


@users_bp.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    user = db.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@users_bp.route('/users/<user_id>', methods=['PUT'])
def modify_user(user_id):
    data = request.json
    updated_user = db.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user)
    return jsonify({"error": "User not found"}), 404


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    message = db.delete_user(user_id)
    return jsonify(message)
