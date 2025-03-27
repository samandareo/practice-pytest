from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30},
}

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404