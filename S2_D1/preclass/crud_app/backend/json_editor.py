import json
import time

# Global variable for file path
file_path = './db.json'

def generate_id () :
    timestamp = str(int(time.time()*1000))
    return timestamp

def read_json_file():
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['students']

def write_json_file(data):
    with open(file_path, 'w') as file:
        json.dump({'students': data}, file, indent=4)

# //////////////////////////////////////////////////////////////
 
def get_data () :
    data = read_json_file()
    return data

def add_data_to_list(new_data):
    data = read_json_file()
    id = generate_id()
    new_data["id"] = id
    data.append(new_data)
    write_json_file(data)

def delete_data_from_list(id):
    data = read_json_file()
    for item in data:
        if item.get('id') == str(id):
            data.remove(item)
            write_json_file(data)
            return
    print("Invalid id.")

def update_data_in_list(id, updated_data):
    data = read_json_file()
    for item in data:
        if item.get('id') == str(id):
            item.update(updated_data)
            write_json_file(data)
            return
    print("Invalid id.")


# //////////////////////////////////////////////
# Example usage

# data = read_json_file()
# print("Initial data:", data)

# new_data = {'name': 'John', 'age': 25}
# add_data_to_list(new_data)

# data = read_json_file()
# print("Data after adding new entry:", data)

# delete_data_from_list(1)

# data = read_json_file()
# print("Data after deleting entry:", data)

# new_data = {'name': 'Piyush', 'age': 25}
# add_data_to_list(new_data)

# updated_data = {'name': 'Alice', 'age': 30}
# update_data_in_list(1, updated_data)

# data = read_json_file()
# print("Data after updating entry:", data)
