from flask import Blueprint, jsonify, request
from application.models import User
from jose import jwt


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/user/signup", methods=["POST"])
def user_signup():
    new_user = request.get_json()

    # Check if the user_email already exists
    existing_user = User.objects(user_email=new_user["user_email"]).first()
    if existing_user:
        return jsonify({"message": "user_Email already exists"}), 400

    # Import bcrypt here to avoid circular import error
    from application import bcrypt

    # Encrypt the password using bcrypt
    hashed_password = bcrypt.generate_password_hash(new_user["user_password"]).decode(
        "utf-8"
    )

    # Create a new user
    user = User(
        user_email=new_user["user_email"],
        user_password=hashed_password,
        user_name=new_user["user_name"],
    )
    user.save()

    return jsonify({"message": "Signup successful"}), 201


@user_routes.route("/user/login", methods=["POST"])
def user_login():
    login_data = request.get_json()

    # Find the user with the provided email
    user = User.objects(user_email=login_data["user_email"]).first()
    if not user:
        return jsonify({"message": "Wrong email"}), 400

    # Import bcrypt here to avoid circular import error
    from application import bcrypt

    # Check if the password is correct
    if bcrypt.check_password_hash(user.user_password, login_data["user_password"]):
        # Generate a token using jsonwebtoken
        token = jwt.encode(
            {"_id": str(user.id)}, "my signature", algorithm="HS256"
        )

        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"message": "Wrong password"}), 400
