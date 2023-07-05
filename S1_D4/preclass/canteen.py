inventory = []
snack = {"name": "", "price": 0, "availability": True}
sales_record = {}

def add_to_inventory(snack):
    for item in inventory:
        if item["name"].lower() == snack["name"].lower().strip():
            print("Snack is already present in the inventory.")
            return
    snack["id"] = len(inventory) + 1
    inventory.append(snack)
    print("Snack added to the inventory:", snack)

def remove_from_inventory(id):
    for item in inventory:
        if item["id"] == id:
            inventory.remove(item)
            print("Snack removed from the inventory.")
            return
    print("No snack matched the ID.")

def update_availability(id):
    for item in inventory:
        if item["id"] == id:
            item["availability"] = not item["availability"]
            print("Snack availability updated.")
            return
    print("No snack matched the ID.")

def update_sales_record(id, qty):
    snack = get_snack_by_id(id)
    if snack:
        if snack["availability"]:
            if id in sales_record:
                sales_record[id] += qty
            else:
                sales_record[id] = qty
            print("Sales record updated.")
        else:
            print("Snack is not available for sale.")
    else:
        print("No snack matched the ID.")


def display_inventory():
    print("Inventory:")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Availability: {item['availability']}")

def display_sales_record():
    print("Sales Record:")
    for id, sales in sales_record.items():
        snack = get_snack_by_id(id)
        if snack:
            print(f"ID: {id}, Name: {snack['name']}, Sales: {sales}")

def get_snack_by_id(id):
    for item in inventory:
        if item["id"] == id:
            return item
    return None

# Main program
while True:
    user_input = input("Enter a command (add/remove/update/sell/display/exit): ")
    if user_input == "add":
        name = input("Enter snack name: ")
        price = float(input("Enter snack price: "))
        availability = input("Is the snack available? (y/n): ").lower() == "y"
        snack = {"name": name, "price": price, "availability": availability}
        add_to_inventory(snack)
    elif user_input == "remove":
        id = int(input("Enter snack ID to remove: "))
        remove_from_inventory(id)
    elif user_input == "update":
        id = int(input("Enter snack ID to update availability: "))
        update_availability(id)
    elif user_input == "sell":
        id = int(input("Enter snack ID to update sales: "))
        qty = int(input("Enter sale quantity: "))
        update_sales_record(id, qty)
    elif user_input == "display":
        display_inventory()
        display_sales_record()
    elif user_input == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid command. Please try again.")
