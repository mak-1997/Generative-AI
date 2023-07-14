from flask import Blueprint, jsonify, request
from application.models import Admin, Order
from jose import jwt


order_routes = Blueprint("order_routes", __name__)


@order_routes.route("/orders", methods=["GET"])
def get_orders():

    # Get the token from the request headers
    token = request.headers.get("Authorization")

    try:
        # Verify and decode the token
        decoded_token = jwt.decode(token, "my signature", algorithms=["HS256"])
        admin_id = decoded_token["_id"]

        # Find the admin with the provided admin_id
        admin = Admin.objects(id=admin_id, is_admin=True).first()

        if not admin:
            return jsonify({"message": "Unauthorized"}), 401

        # Get all orders
        orders = Order.objects().to_json()
        return orders, 200

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401

@order_routes.route("/orders", methods=["POST"])
def add_new_order () :
    
    token = request.headers.get("Authorization")
    new_order = request.get_json()
    try :
        # Verify and decode the token
        decoded_token = jwt.decode(token, "my signature", algorithms=["HS256"])
        user_id = decoded_token["_id"]
        order = Order(**new_order, user_id = user_id)
        order.save()
        return order.to_json(), 201

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
    
