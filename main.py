from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def root():
    return 'Home'

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {'id':user_id, 'name':'test', 'telefono':'3174783046'}
    query =request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)