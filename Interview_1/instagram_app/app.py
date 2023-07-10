from flask import Flask, request
import time

app = __name__


def generate_id () :
    print(time.time())

generate_id()

@app.route("/create", methods = ["POST"])
def create () :
    if request.method == "POST" :
        new_post = {

        }

if __name__ == "__main__" :
    app.run()
