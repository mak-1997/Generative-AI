from flask import Flask, request
from flask_cors import CORS
from json_editor import (
    get_data,
    add_data_to_list,
    delete_data_from_list,
    update_data_in_list,
)

app = Flask(__name__)
CORS(app)

@app.route("/read", methods=["GET"])
def read():
    if request.method == "GET" :
        data = get_data()
        print(data)
        return data
    return "wrong method !!"

@app.route("/create", methods=["GET", "POST"])
def create() :
    if request.method == "POST" :
        new_data = request.get_json()
        print(new_data)
        add_data_to_list(new_data)
        data = get_data()
        return data
    return "wrong method !!"

@app.route("/update/<int:id>", methods = ["PUT"])
def update (id) :
    if request.method == "PUT" :
        updated_data = request.get_json()
        update_data_in_list(id, updated_data)
        data = get_data()
        return data
    return "wrong method !!"

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id) :
    if request.method == "DELETE" :
        delete_data_from_list(id)
        data = get_data()
        return data
    


if __name__ == "__main__":
    app.run()
