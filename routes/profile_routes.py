from flask import Blueprint, jsonify, request
from database import database as db

profiles_bp = Blueprint('profiles', __name__)


@profiles_bp.route('/profiles', methods=['GET'])
def fetch_profiles():
    profiles = db.get_all_profiles()
    return jsonify(profiles)


@profiles_bp.route('/profiles', methods=['POST'])
def add_profile():
    data = request.json
    new_profile = db.create_profile(data)
    return jsonify(new_profile), 201


@profiles_bp.route('/profiles/<profile_id>', methods=['GET'])
def get_single_profile(profile_id):
    profile = db.get_profile_by_id(profile_id)
    if profile:
        return jsonify(profile)
    return jsonify({"error": "Profile not found"}), 404


@profiles_bp.route('/profiles/<profile_id>', methods=['PUT'])
def modify_profile(profile_id):
    data = request.json
    updated_profile = db.update_profile(profile_id, data)
    if updated_profile:
        return jsonify(updated_profile)
    return jsonify({"error": "Profile not found"}), 404


@profiles_bp.route('/profiles/<profile_id>', methods=['DELETE'])
def remove_profile(profile_id):
    message = db.delete_profile(profile_id)
    return jsonify(message)
