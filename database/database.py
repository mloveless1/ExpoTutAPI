from pymongo import MongoClient

# Connect to MongoDB and define collections
client = MongoClient('localhost', 27017)
db = client.DateApp
profiles_collection = db.profiles
users_collection = db.users
messages_collection = db.messages


# Profiles CRUD operations
def create_profile(data):
    """Create a new profile and return the inserted profile."""
    profile_id = profiles_collection.insert_one(data).inserted_id
    return get_profile_by_id(profile_id)


def get_all_profiles():
    """Return all profiles."""
    return list(profiles_collection.find({}))


def get_profile_by_id(profile_id):
    """Return a specific profile by ID."""
    return profiles_collection.find_one({"_id": profile_id})


def update_profile(profile_id, data):
    """Update a profile and return the updated profile."""
    profiles_collection.update_one({"_id": profile_id}, {"$set": data})
    return get_profile_by_id(profile_id)


def delete_profile(profile_id):
    """Delete a profile by ID."""
    profiles_collection.delete_one({"_id": profile_id})
    return {"message": "Profile deleted successfully"}


# Users CRUD operations
def create_user(data):
    """Create a new user and return the inserted user."""
    user_id = users_collection.insert_one(data).inserted_id
    return get_user_by_id(user_id)


def get_all_users():
    """Return all users."""
    return list(users_collection.find({}))


def get_user_by_id(user_id):
    """Return a specific user by ID."""
    return users_collection.find_one({"_id": user_id})


def update_user(user_id, data):
    """Update a user and return the updated user."""
    users_collection.update_one({"_id": user_id}, {"$set": data})
    return get_user_by_id(user_id)


def delete_user(user_id):
    """Delete a user by ID."""
    users_collection.delete_one({"_id": user_id})
    return {"message": "User deleted successfully"}


# Messages CRUD operations

def create_message(data):
    """Create a new message and return the inserted profile."""
    message_id = messages_collection.insert_one(data).inserted_id
    return get_message_by_id(message_id)


def get_all_messages():
    """Return all messages."""
    return list(messages_collection.find({}))


def get_message_by_id(message_id):
    """Return a specific message by message id."""
    return messages_collection.find_one({"_id": message_id})


def get_messages_by_receiver_id(receiver_id):
    """Return all messages sent to this receiver"""
    return messages_collection.find({"receiver_id": receiver_id})


def get_messages_by_sender_id(sender_id):
    """Return all messages sent by this sender"""
    return messages_collection.find({"sender_id": sender_id})


def update_message(message_id, data):
    """Update a message and return the updated message."""
    messages_collection.update_one({"_id": message_id}, {"$set": data})
    return get_message_by_id(message_id)


def delete_message(message_id):
    """Delete a message by ID."""
    users_collection.delete_one({"_id": message_id})
    return {"message": "Message deleted successfully"}
