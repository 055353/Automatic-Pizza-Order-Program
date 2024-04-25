# Building automatic pizza order program

# Greeting
print("Welcome to Python Pizza Deliveries")

# Ask for the size of pizza
size = input("What size of pizza do you want? S, M, L: ")
# Ask if the user wants extra pepperoni
add_pepperoni = input("Do you want extra pepperoni? Y or N: ")
# Ask if the user wants extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Define prices
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small_pizza = 2
pepperoni_for_medium_or_large_pizza = 3
extra_cheese_for_small_pizza = 1
extra_cheese_for_medium_or_large_pizza = 2

# Calculate bill based on user selections

# For small pizza
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is $" + str(small_pizza + pepperoni_for_small_pizza + extra_cheese_for_small_pizza) + ".")
        else:
            print("Your final bill is $" + str(small_pizza + pepperoni_for_small_pizza) + ".")
    elif extra_cheese == "Y":
        print("Your final bill is $" + str(small_pizza + extra_cheese_for_small_pizza) + ".")
    else:
        print("Your final bill is $" + str(small_pizza) + ".")

# For medium pizza
elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is $" + str(medium_pizza + pepperoni_for_medium_or_large_pizza + extra_cheese_for_medium_or_large_pizza) + ".")
        else:
            print("Your final bill is $" + str(medium_pizza + pepperoni_for_medium_or_large_pizza) + ".")
    elif extra_cheese == "Y":
        print("Your final bill is $" + str(medium_pizza + extra_cheese_for_medium_or_large_pizza) + ".")
    else:
        print("Your final bill is $" + str(medium_pizza) + ".")

# For large pizza
elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print("Your final bill is $"
