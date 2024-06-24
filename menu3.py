banner = """
  __        __   _                                        
  \ \      / /__| | ___ ___  _ __ ___   ___  
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \ V  V /  __/ | (_| (_) | | | | | |  __/ 
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
"""

print(banner)
print("Welcome to Grab A Bite.")

print("From which section would you like to order? ")

i = 1
menu_items = {}

menu = {
    "Quick Bites": {
        "Chips": 0.99,
        "Banana": 0.69,
        "Apple": 1.49,
        "Granola bar": 1.99
    },
    "Full Eats": {
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
    "Beverages": {
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
    "Sweets": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "Oreo": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Display menu categories
for key in menu.keys():
    print(f"{i}: {key}")
    menu_items[i] = key
    i += 1

while True:
    menu_category = input("Type menu number: ")
    if menu_category.isdigit():
        menu_category = int(menu_category)
        if menu_category in menu_items.keys():
            menu_category_name = menu_items[menu_category]
            print(f"You selected {menu_category_name}")

            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            selected_menu_items = {}

            # Display items in selected menu category
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        item_name = f"{key} - {key2}"
                        print(f"{i: <6} | {item_name: <24} | ${value2:.2f}")
                        selected_menu_items[i] = {
                            "Item name": item_name,
                            "Price": value2
                        }
                        i += 1
                else:
                    print(f"{i: <6} | {key: <24} | ${value:.2f}")
                    selected_menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            order = {}
            while True:
                menu_item_number = input("Input menu item number ('q' to quit): ")
                if menu_item_number.lower() == 'q':
                    break
                if menu_item_number.isdigit():
                    menu_item_number = int(menu_item_number)
                    if menu_item_number in selected_menu_items:
                        quantity = int(input(f"How many {selected_menu_items[menu_item_number]['Item name']}s would you like? "))
                        if quantity > 0:
                            item_name = selected_menu_items[menu_item_number]['Item name']
                            if item_name in order:
                                order[item_name] += quantity
                            else:
                                order[item_name] = quantity
                        else:
                            print("Please enter a valid quantity (greater than zero).")
                    else:
                        print("Invalid item number, please try again.")
                else:
                    print("Invalid input, please enter a valid item number.")

            # Print receipt
            print("\n============= Receipt =============")
            print("This is what we are preparing for you.\n")
            total_price = 0
            for item, quantity in order.items():
                price_per_item = next((selected_menu_items[key]['Price'] for key in selected_menu_items if selected_menu_items[key]['Item name'] == item), None)
                if price_per_item is not None:
                    item_total = price_per_item * quantity
                    total_price += item_total
                    print(f"{item}: {quantity} x ${price_per_item:.2f} = ${item_total:.2f}")
                else:
                    print(f"Price information not found for {item}")

            print(f"Total: ${total_price:.2f}")
            print("==================================\n")
            print("Thank you for ordering with us")

            while True:
                keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
                if keep_ordering.lower() in ['y', 'n']:
                    break
                else:
                    print("Invalid input, please enter 'Y' or 'N'.")
            if keep_ordering.lower() == 'n':
                break
        else:
            print("Invalid menu number, please try again.")
    else:
        print("Invalid input, please enter a valid menu number.")

print("Thank you for visiting!")