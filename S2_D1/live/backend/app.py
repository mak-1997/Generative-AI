from flask import Flask, request, jsonify
from flask_cors import CORS
from json_editor import (
    get_data,
    add_new_dish,
    delete_dish,
    update_dish,
    add_new_order,
    update_order,
)

app = Flask(__name__)
CORS(app)

# DISHES//////////////////////////////////////////////


@app.route("/get_dishes", methods=["GET"])
def get_dishes():
    if request.method == "GET":
        data = get_data("dishes")
        return data
    return jsonify({"msg" :"request method should be GET"}), 400


@app.route("/add_dish", methods=["POST"])
def add_dish():
    if request.method == "POST":
        new_dish = request.get_json()
        print(new_dish)
        add_new_dish(new_dish)
        data = get_data("dishes")
        return data
    return jsonify({"msg" :"request method should be POST"}), 400


@app.route("/remove_dish/<int:id>", methods=["DELETE"])
def remove_a_dish(id):
    if request.method == "DELETE":
        delete_dish(id)
        data = get_data("dishes")
        return data
    return jsonify({"msg" :"request method should be DELETE"}), 400


@app.route("/update_dish/<int:id>", methods=["PUT"])
def update_a_dish(id):
    if request.method == "PUT":
        updated_dish = request.get_json()
        update_dish(id, updated_dish)
        data = get_data("dishes")
        return data
    return jsonify({"msg" :"request method should be PUT"}), 400


# ORDERS/////////////////////////////////////////////////


@app.route("/get_orders", methods=["GET"])
def get_orders():
    if request.method == "GET":
        data = get_data("orders")
        return data
    return jsonify({"msg" :"request method should be GET"}), 400


@app.route("/add_order", methods=["POST"])
def add_orders():
    if request.method == "POST":
        new_order = request.get_json()
        # if new_order["availability"] == "No" :
        #     return jsonify({"msg" :"Dish is not available right now"}), 400
        new_order["status"] = "prepairing"
        add_new_order(new_order)
        data = get_data("orders")
        return data
    return jsonify({"msg" :"request method should be POST"}), 400


@app.route("/update_order/<int:id>", methods=["PUT"])
def update_an_order(id):
    if request.method == "PUT":
        updated_order = request.get_json()
        update_order(id, updated_order)
        data = get_data("orders")
        return data
    return jsonify({"msg" :"request method should be PUT"}), 400



if __name__ == "__main__":
    app.run()

