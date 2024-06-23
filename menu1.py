banner = """
  __        __   _                                        
  \ \      / /__| | ___ ___  _ __ ___   ___  
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \ V  V /  __/ | (_| (_) | | | | | |  __/ 
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
"""

# Food Truck Menu
print(banner)
print("Welcome to Grab A Bite.")

print ("From which section would you like to order? ")
i = 1
menu_items = {}
Price = []
Total = []
menu = {
    "Quick Bites": {
        "Chips": .99,
        "Banana": .69,
        "Apple": .49,
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

for key in menu.keys():
    print(f"{i}: {key}")
    menu_items[i] = key
    i += 1

while True:
  menu_category = input("Type menu number: ")
  if menu_category.isdigit():
    if int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")

        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        selected_menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if type(value) is dict:
                for key2, value2 in value.items():
                     num_item_spaces = 24 - len(key + key2) - 3
                     item_spaces = " " * num_item_spaces
                     print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                     selected_menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                     i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
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
                        if selected_menu_items[menu_item_number]['Item name'] in order:
                            order[selected_menu_items[menu_item_number]['Item name']] += quantity
                        else:
                            order[selected_menu_items[menu_item_number]['Item name']] = quantity
                    else:
                        print("Please enter a valid quantity (greater than zero).")
                else:
                    print("Invalid item number, please try again.")
            else:
                print("Invalid input, please enter a valid item number.")

  while True:
            keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
            if keep_ordering != 'y':  
             print("\nYour order:")
             total_price = 0
             print("This is what we are preparing for you.\n")
             def generate_receipt(order, selected_menu_items):
               print("\n===== Receipt =====")
             for item, quantity in order.items():
                price_per_item = selected_menu_items[[key for key, value in selected_menu_items.items() if value['Item name'] == item][0]]['Price']
                item_total = price_per_item * quantity
                total_price += item_total
                print(f"{item}: {quantity} x ${price_per_item} = ${item_total:.2f}")
            print(f"Total: ${total_price:.2f}")
            print("==================\n")
            print("Thank you for ordering with us!")
            
    

                
     
                 
        




            
                

        

        


            

                         
                



                     

        


        
                     
            
                 
                
    
    


     
   
    

   

       


        



    
    





     
     
  
     








     





