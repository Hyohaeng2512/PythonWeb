import firebase_admin
from firebase_admin import credentials
from firebase_config import firebase_config
import pyrebase

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        user = auth.create_user_with_email_and_password(email, password)
        return jsonify({"message": "User created successfully", "uid": user['localId']}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return jsonify({"message": "Login successful", "token": user['idToken']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = {
        "name": data.get("name"),
        "price": data.get("price"),
        "description": data.get("description"),
         "image": data.get("image")
    }
    db.child("products").push(product)
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = db.child("products").get().val()
    return jsonify(products), 200

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    db.child("products").child(product_id).update(data)
    return jsonify({"message": "Product updated successfully"}), 200

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    db.child("products").child(product_id).remove()
    return jsonify({"message": "Product deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)