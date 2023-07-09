import json
import time

file_path = "./db.json"


def generate_id():
    timestamp = str(int(time.time() * 1000))
    return timestamp


def read_json_file(endpoint=""):
    with open(file_path, "r") as file:
        data = json.load(file)
    if endpoint == "":
        return data
    return data[endpoint]


def write_json_file(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# //////////////////////////////////////////////////////////////


def get_data(endpoint=""):
    data = read_json_file(endpoint)
    return data


# Dishes//////////////////////////////////////


def add_new_dish(new_dish):
    data = read_json_file()
    id = generate_id()
    new_dish["id"] = id
    data["dishes"].append(new_dish)
    write_json_file(data)


def delete_dish(id):
    data = read_json_file()
    for item in data["dishes"]:
        if item.get("id") == str(id):
            data["dishes"].remove(item)
            write_json_file(data)
            return
    print(f"invalid id: {id}")


def update_dish(id, updated_data):
    data = read_json_file()
    for item in data["dishes"]:
        if item.get("id") == str(id):
            item.update(updated_data)
            write_json_file(data)
            return
    print("Invalid id.")


# Orders//////////////////////////////////////

def add_new_order(new_order) : 
    data = read_json_file()
    id = generate_id()
    new_order["id"] = id
    data["orders"].append(new_order)
    write_json_file(data)


def update_order(id, updated_data):
    data = read_json_file()
    for item in data["orders"]:
        if item.get("id") == str(id):
            item.update(updated_data)
            write_json_file(data)
