from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (DO NOT include test data when pushing)
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Return all usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Get specific user by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


# Add new user (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    # Ensure request contains JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Validate username presence
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to dictionary
    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()