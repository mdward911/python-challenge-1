# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Ask customer to input menu item number
            while True:
                menu_choice = input("Enter item number to order or '0' to go back to menu: ")

                # Check if the customer typed a number
                if menu_choice.isdigit():
                    menu_choice = int(menu_choice)

                    # Check if the menu selection is in the menu items
                    if 0 < menu_choice <= len(menu_items):
                        # Store the item name as a variable
                        item_name = menu_items[menu_choice]["Item name"]

                        # Ask the customer for the quantity of the menu item
                        quantity = input(f"How many '{item_name}' would you like to order? ")
                        
                        # Check if the quantity is a number, default to 1 if not
                        if quantity.isdigit():
                            quantity = int(quantity)
                        else:
                            print("Invalid quantity. Defaulting to 1.")
                            quantity = 1

                        # Add the item name, price, and quantity to the order list
                        order_list.append({
                            "Item name": item_name,
                            "Price": menu_items[menu_choice]["Price"],
                            "Quantity": quantity
                        })

                        # Confirm the order
                        print(f"{quantity} '{item_name}' added to your order.")

                    elif menu_choice == 0:
                        # Go back to menu selection
                        break
                    else:
                        # Tell the customer their input isn't valid
                        print("Invalid menu item number. Please try again.")

                else:
                    # Tell the customer they didn't select a number
                    print("Invalid input. Please enter a number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        # Check the customer's input
        if keep_ordering == 'y' or keep_ordering == 'yes':
            # Keep ordering
            break
        elif keep_ordering == 'n' or keep_ordering == 'no':
            # Exit the keep ordering question loop
            place_order = False
            break
        else:
            # Tell the customer to try again
            print("Invalid input. Please enter (Y)es or (N)o.")

# Print out the customer's order
print("\nThis is what we are preparing for you.\n")

total_cost = 0

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order
for item in order_list:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    item_spaces = " " * num_item_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price:.2f} | {quantity}")

    # Calculate total cost
    total_cost += price * quantity

# Print total cost of the order
print(f"\nTotal cost: ${total_cost:.2f}")