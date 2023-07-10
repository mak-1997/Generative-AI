from flask import Flask, request, jsonify
import time

app = Flask(__name__)

data = {}

def generate_id () :
    t = time.time()
    id = int(t*1000)
    print(id)

# generate_id()

@app.route("/create", methods = ["POST"])
def create () :
    if request.method == "POST" :
       new_post = request.get_json()
       id= generate_id()
       data[id] = new_post
       return data
    return "Wrong Method", 400

@app.route("/view", methods=["GET"])
def read() :
    if request.method == "GET" :
        return data
    return "Wrong Method", 400

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_post(id) :
    if request.method == "DELETE" :
        if id in data :
            del data[id]
            return data
        return "Post Id not present in database"
    return "Wrong Method"

if __name__ == "__main__" :
    app.run()
