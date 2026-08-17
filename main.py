# welcome message with equals - might do ascii art in future maybe?

print("===============================")
print("===============================")
print("  Welcome to Robo-Roast Cafe!  ")
print("===============================")
print("===============================")

# welcome them to cafe and ask for name

print("Hope you are having a great day! \n")

name_check = False

while name_check == False:
    name = input("What is your name?\n")
    confirm_name = input("Just to confirm, was that " + name + "? (y/n)\n")
    if confirm_name == "y":
        name_check = True
    else:
        print("Oh - very sorry!")

print("Great to meet you, " + name + "!")

print("Lets get you a drink! \nWhat were you looking for today?\n")

drinks = ["Latte", "Iced Latte", "Hot Chocolate", "English Breakfast Tea"]
drinks_prices = [3.75, 4.20, 4.00, 2.80]
drinks_number_track = -1

for item in drinks:
    drinks_number_track = drinks_number_track + 1
    print(str(drinks_number_track + 1) + ". " + item + " ---> £" + str(drinks_prices[drinks_number_track]))

drink_check = False

while drink_check == False:
    drink_order = int(input("\nWhat number drink would you like? "))
    if drink_order >= 1 and drink_order <= 4:
        drink_check = True
    else:
        print("Very sorry - but I don't know that drink! ")
