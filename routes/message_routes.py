from flask import Blueprint, jsonify, request
from models import Message
from database import database as db

messages_bp = Blueprint('messages', __name__)


@messages_bp.route('/messages/<receiver_id>', methods=['GET'])
def fetch_messages(receiver_id):
    if receiver_id:
        messages = db.get_messages_by_receiver_id(receiver_id)
        for message in messages:
            message['_id'] = str(message['_id'])  # Convert ObjectId to string
            message['timestamp'] = message['timestamp'].isoformat()  # Convert datetime to ISO format string

    else:
        return jsonify({"Error": "User ID is required"}), 400
    if messages:
        return jsonify(messages)
    else:
        return jsonify({"error": "Messages not found"}), 404


@messages_bp.route('/messages', methods=['POST'])
def add_profile():
    data = request.json
    new_message = db.create_message(data)
    return jsonify(new_message), 201


""""@messages_bp.route('/messages/<message_id>', methods=['GET'])
def get_single_message(message_id):
    message = db.get_message_by_id(message_id)
    if message:
        return jsonify(message)
    return jsonify({"error": "Message not found"}), 404"""


@messages_bp.route('/messages/<message_id>', methods=['PUT'])
def modify_message(message_id):
    data = request.json
    updated_message = db.update_message(message_id, data)
    if updated_message:
        return jsonify(updated_message)
    return jsonify({"error": "Message not found"}), 404


@messages_bp.route('/messages/<message_id>', methods=['DELETE'])
def remove_message(message_id):
    message = db.delete_message(message_id)
    return jsonify(message)
