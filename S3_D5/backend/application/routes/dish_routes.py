from flask import request, jsonify, Blueprint
from application.models import Dish

dish_routes = Blueprint('dish_routes', __name__)

@dish_routes.route("/dishes", methods=["GET"])
def get_dishes():
    if request.method == "GET":
        dishes = Dish.objects().to_json()
        return dishes, 200  # Returning JSON data directly with status code 200
    return jsonify({"msg": "Request method should be GET"}), 400  # Returning JSON error response with status code 400

@dish_routes.route("/dishes", methods=["POST"])
def add_dish():
    new_dish = request.get_json()
    dish = Dish(**new_dish)
    dish.save()
    return dish.to_json(), 201  # Returning JSON data directly with status code 201

@dish_routes.route("/dishes/<ObjectId:_id>", methods=["PUT"])
def update_dish(_id):
    updated_dish = request.get_json()
    dish = Dish.objects(id=_id).first()

    if dish:
        # Update the dish fields
        for field, value in updated_dish.items():
            setattr(dish, field, value)

        dish.save()
        return dish.to_json(), 200  # Returning updated dish data with status code 200
    else:
        return jsonify({"msg": "Dish not found"}), 404  # Returning error response with status code 404

@dish_routes.route("/dishes/<ObjectId:_id>", methods=["DELETE"])
def delete_dish(_id):
    dish = Dish.objects(id=_id).first()

    if dish:
        dish.delete()
        return jsonify({"msg": "Dish deleted"}), 200  # Returning success response with status code 200
    else:
        return jsonify({"msg": "Dish not found"}), 404  # Returning error response with status code 404
