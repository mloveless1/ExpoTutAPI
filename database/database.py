from pymongo import MongoClient

# Connect to MongoDB and define collections
client = MongoClient('localhost', 27017)
db = client.DateApp
profiles_collection = db.profiles
users_collection = db.users


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
