from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (DO NOT include test data)
users = {}


# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Status route
@app.route("/status")
def status():
    return "OK"


# Return all usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Get a specific user
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


# Add a user
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    # IMPORTANT: return only the user object with default 200
    return jsonify(data)


if __name__ == "__main__":
    app.run()