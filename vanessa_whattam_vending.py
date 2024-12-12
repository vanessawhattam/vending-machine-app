# Product names with codes as the variable name
A1 = "PB&J"
B2 = "Flatbread"
C3 = "Rice"
D4 = "Pancakes"
E5 = "Waffles"

# These are the prices for each item
pbj_price = 1.5
flatbread_price = 2.75
rice_price = 2
pancake_price = 3.25
waffle_price = 2.5

# These will increase by 1 each time the item is selected
pbj = 0
flatbread = 0
rice = 0
pancake = 0
waffle = 0 

# Initiate a variable for our total cost
total_cost = 0

# Initiate a variable for our continuance statement
hungry = 1

# Initiate the loop
while True:
    # Provide the initial order options
    order = input(f'''
                 Hello! Welcome to the carb machine! \n

        Please select an item from the menu below:\n

      | Code | Product    | Price |\n
      | A1   | {A1}       | ${pbj_price}  |\n
      | B2   | {B2}       | ${flatbread_price} |\n
      | C3   | {C3}       | ${rice_price}   |\n
      | D4   | {D4}       | ${pancake_price} |\n
      | E5   | {E5}       | ${waffle_price}   |\n


      What would you like to order? Please enter the code for your desired item:
  ''')

    # If they want A1
    if order == "A1":
        # Ask for the quantity
        quantity = input("How many do you want?")

        # Make sure they gave something numeric
        if quantity.isdigit():
            # Then turn it into a number
            quantity = float(quantity)

            # Add 1 to our PBJ variable
            pbj += quantity
            # Add the price to the total cost of the order
            total_cost += quantity*pbj_price

            # Confirm the quantity and item. Ask if they want more
            hungry = input(f"You want {quantity} of {A1}. Your total so far is ${total_cost}. Want more? 1 for yes, 2 for no.")

            # Make sure the input is numeric
            if hungry.isdigit():
                # Turn it into a number
                hungry = float(hungry) 
                
                # If still hungry
                if hungry == 1:
                    continue
                # If not hungry
                elif hungry == 2:
                    # Confirm the quantities and total cost
                    print(f'''
                    Thanks for your order. You ordered the following: 

                    PB&J - {pbj}
                    Flatbread - {flatbread}
                    Rice - {rice}
                    Pancakes - {pancake}
                    Waffle - {waffle}

                    Your total cost is ${round(total_cost, 2)}. Please come again.
                    ''')
                    break
                # If they enter a number besides 1 or 2
                else:
                    input("That is not an option. Please try again.")
            # If they don't enter a number when asked if still hungry, make 'em do it again
            else:
                input("That is not an option. Please try again.")
        # If they didn't enter a numeric value when asked for the quantity make 'em do it again
        else:
            input("That is not an option. Please try again.")

    # Same but for flatbreads 
    elif order == "B2":
        quantity = input("How many do you want?")

        if quantity.isdigit():
            quantity = float(quantity)

            flatbread += quantity
            total_cost += quantity*flatbread_price

            hungry = input(f"You want {quantity} of {B2}. Your total so far is ${total_cost}. Want more? 1 for yes, 2 for no.")
            if hungry.isdigit():
                hungry = float(hungry) 
                
                if hungry == 1:
                    continue
                elif hungry == 2:
                    print(f'''
                    Thanks for your order. You ordered the following: 

                    PB&J - {pbj}
                    Flatbread - {flatbread}
                    Rice - {rice}
                    Pancakes - {pancake}
                    Waffle - {waffle}

                    Your total cost is ${round(total_cost, 2)}. Please come again.
                    ''')
                    break
                else:
                    input("That is not an option. Please try again.")
            else:
                input("That is not an option. Please try again.")
        else:
            input("That is not an option. Please try again.")

    # same but for rice
    elif order == "C3":
        quantity = input("How many do you want?")

        if quantity.isdigit():
            quantity = float(quantity)

            rice += quantity
            total_cost += quantity*rice_price

            hungry = input(f"You want {quantity} of {C3}. Your total so far is ${total_cost}. Want more? 1 for yes, 2 for no.")
            if hungry.isdigit():
                hungry = float(hungry) 
                
                if hungry == 1:
                    continue
                elif hungry == 2:
                    print(f'''
                    Thanks for your order. You ordered the following: 

                    PB&J - {pbj}
                    Flatbread - {flatbread}
                    Rice - {rice}
                    Pancakes - {pancake}
                    Waffle - {waffle}

                    Your total cost is ${round(total_cost, 2)}. Please come again.
                    ''')
                    break
                else:
                    input("That is not an option. Please try again.")
            else:
                input("That is not an option. Please try again.")
        else:
            input("That is not an option. Please try again.")

    # Same but for Pancakes
    elif order == "D4":
        quantity = input("How many do you want?")

        if quantity.isdigit():
            quantity = float(quantity)

            pancake += quantity
            total_cost += quantity*pancake_price

            hungry = input(f"You want {quantity} of {D4}. Your total so far is ${total_cost}. Want more? 1 for yes, 2 for no.")
            if hungry.isdigit():
                hungry = float(hungry) 
                
                if hungry == 1:
                    continue
                elif hungry == 2:
                    print(f'''
                    Thanks for your order. You ordered the following: 

                    PB&J - {pbj}
                    Flatbread - {flatbread}
                    Rice - {rice}
                    Pancakes - {pancake}
                    Waffle - {waffle}

                    Your total cost is ${round(total_cost, 2)}. Please come again.
                    ''')
                    break
                else:
                    input("That is not an option. Please try again.")
            else:
                input("That is not an option. Please try again.")
        else:
            input("That is not an option. Please try again.")

    # Same but for waffles
    elif order == "E5":
        quantity = input("How many do you want?")

        if quantity.isdigit():
            quantity = float(quantity)

            waffle += quantity
            total_cost += quantity*waffle_price

            hungry = input(f"You want {quantity} of {E5}. Your total so far is ${total_cost}. Want more? 1 for yes, 2 for no.")
            if hungry.isdigit():
                hungry = float(hungry) 
                
                if hungry == 1:
                    continue
                elif hungry == 2:
                    print(f'''
                    Thanks for your order. You ordered the following: 

                    {A1} - {pbj}
                    {B2} - {flatbread}
                    {C3} - {rice}
                    {D4} - {pancake}
                    {E5} - {waffle}

                    Your total cost is ${round(total_cost, 2)}. Please come again.
                    ''')
                    break
                else:
                    input("That is not an option. Please try again.")
            else:
                input("That is not an option. Please try again.")
        else:
            input("That is not an option. Please try again.")

    # In case they entered something other than approved codes, make 'em do it again   
    else:
        input("That is not an option. Please try again.")

    