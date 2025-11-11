from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"name": "John", "id": 1},
    {"name": "Michael", "id": 2},
]

# GET 전체 사용자 조회
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET 특정 사용자 조회
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
