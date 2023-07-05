# 1. **Menu Mastery**: Your system should enable Zesty Zomato to manage their mouth-watering menu of dishes. Each dish will have unique attributes, such as dish ID, dish name, price, and availability (yes or no).
# 2. **User Interaction Euphoria**: Zesty Zomato staff should be able to perform the following tasks:
#     - Add a delicious new dish to the menu.
#     - Remove a dish that is no longer served.
#     - Update the availability of a dish based on their dynamic kitchen operations.
#     - Take a new order from a ravenous customer.
#     - Update the status of an order as it goes from 'received' to 'preparing', then 'ready for pickup' and finally 'delivered'.
#     - Review all the orders to ensure everything is going as per plan.
#     - An exit option to wind up the day's operations.
# 3. **Taking Orders**: When a customer places an order, Zesty Zomato staff should be able to enter the customer's name and the dish IDs. The system should check whether each dish is available. If so, it should process the order, assigning a unique order ID and setting the initial order status as 'received'.
# 4. **Order Updates**: When the status of an order changes, staff should be able to enter the unique order ID and update the new status.
# 5. **Edge Case Excellence**: The system should be smart enough to handle invalid inputs and edge cases, such as ordering a dish that doesn't exist or isn't available.

menu = []  # To store the menu of dishes
orders = []  # To store the orders
dish_id_counter = 1  # To generate unique dish IDs

def generate_dish_id():
    global dish_id_counter
    dish_id = dish_id_counter
    dish_id_counter += 1
    return dish_id

def add_dish(dish_name, price):
    for dish in menu:
        if dish["name"] == dish_name:
            print("Dish with the same name already exists. Please enter a different name.")
            return

    dish_id = generate_dish_id()
    dish = {"id": dish_id, "name": dish_name, "price": price, "availability": True}
    menu.append(dish)
    print(f"Dish '{dish_name}' added successfully to the menu. Dish ID: {dish_id}")

def remove_dish(dish_id):
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            print(f"Dish with ID {dish_id} removed successfully from the menu.")
            return
        
    print("Dish ID not found. Please enter a valid ID.")

def update_dish_availability(dish_id, availability):
    for dish in menu:
        if dish["id"] == dish_id:
            dish["availability"] = availability
            print("Dish availability updated successfully.")
            return

    print("Dish ID not found. Please enter a valid ID.")

def take_order(customer_name, dish_names):
    order_id = len(orders) + 1
    order_status = "received"
    order_items = []

    for dish_name in dish_names:
        found = False
        for dish in menu:
            if dish["name"] == dish_name:
                if dish["availability"]:
                    order_items.append(dish)
                    found = True
                else:
                    print(f"Dish '{dish_name}' is not available. Skipping this item.")
                break

        if not found:
            print(f"Dish '{dish_name}' does not exist. Skipping this item.")

    if order_items:
        order = {
            "id": order_id,
            "customer_name": customer_name,
            "order_items": order_items,
            "status": order_status
        }
        orders.append(order)
        print(f"Order taken successfully. Order ID: {order_id}")
    else:
        print("No items available for order. Please check the menu.")

def update_order_status(order_id, new_status):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = new_status
            print("Order status updated successfully.")
            return

    print("Order ID not found. Please enter a valid ID.")

def review_orders():
    if orders:
        print("All Orders:")
        for order in orders:
            print(f"Order ID: {order['id']}")
            print(f"Customer Name: {order['customer_name']}")
            print("Order Items:")
            for dish in order["order_items"]:
                print(f"- Dish ID: {dish['id']}, Dish Name: {dish['name']}")
            print(f"Status: {order['status']}")
            print("-------------------")
    else:
        print("No orders to review.")

def run_restaurant_system():
    while True:
        print("========= Zesty Zomato =========")
        print("1. Add Dish to Menu")
        print("2. Remove Dish from Menu")
        print("3. Update Dish Availability")
        print("4. Take Order")
        print("5. Update Order Status")
        print("6. Review Orders")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            dish_name = input("Enter Dish Name: ").strip().lower()
            price = input("Enter Price: ")
            add_dish(dish_name, price)
        elif choice == "2":
            dish_id = int(input("Enter Dish ID to remove: "))
            remove_dish(dish_id)
        elif choice == "3":
            dish_id = int(input("Enter Dish ID to update availability: "))
            availability = input("Enter Availability (y/n): ")
            update_dish_availability(dish_id, availability.lower() == "y")
        elif choice == "4":
            customer_name = input("Enter Customer Name: ").strip()
            dish_names = [dish.strip().lower() for dish in input("Enter Dish Names (comma-separated): ").split(",")]
            take_order(customer_name, dish_names)
        elif choice == "5":
            order_id = int(input("Enter Order ID to update status: "))
            new_status = input("Enter New Status(preparing/ready for pickup /delivered): ").strip()
            update_order_status(order_id, new_status)
        elif choice == "6":
            review_orders()
        elif choice == "7":
            print("Exiting Zesty Zomato. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")



run_restaurant_system()



