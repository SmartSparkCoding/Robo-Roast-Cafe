import random

def payment(total):
    print("========== £" + str(total) + " ==========")
    print("How would you like to pay?\n")
    print("1. Apple Pay / Google Pay")
    print("2. Contactless Card")
    print("3. Cash (We have a £2 charge because the owner doesn't like cash)")
    print("4. Hack Club Free Voucher")
    payment_check = False
    while payment_check == False:
        payment_choice = int(input())
        if payment_choice >= 1 and payment_choice <= 4:
            if payment_choice == 1 or payment_choice == 2:
                print("Just tap here please!")
                print("Thank you - here are your items!!\n Thanks for visiting!")
                exit()
            elif payment_choice == 3:
                total = total + 2
                print("So because you chose cash, your new total is £" + str(total) + "!")
                print("Thank you for your payment - Thanks for visiting!!")
                exit()
            else: 
                print("Well - its great you are part of Hack Club! ")
                print("Have your order for free! Thanks for visiting!")
                exit()
        else:
            print("Thats not a valid option of payment!")

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

if name == "sue" or name == "Sue" or name == "Sue Sue Sue" or name == "sue sue sue": 
    print("Hey SUE SUE SUE - I am Linda!")
    weight = int(input("HOW MUCH DO YOU WEIIIIIGH?"))

print("Great to meet you, " + name + "!")

print("Let's get you a drink! \nWhat were you looking for today?\n")

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

drink_order = drink_order - 1

number_of_drinks = int(input("How many " + drinks[drink_order] + "s would you like?\n"))

total = drinks_prices[drink_order] * number_of_drinks

extra_item = random.randint(0, 5)

extra_item_list = ["muffin", "cupcake", "brownie", "cookie", "chocolate twist", "pain au chocolat"]
extra_item_prices = [3.50, 2.85, 3.25, 2.50, 2.90, 3.40]

extra_item_choice = input("So far, your total comes to: £" + str(total) + " - would you like a " + extra_item_list[extra_item] + " with that? (y/n)\n")

if extra_item_choice == "y":
    extra_item_amount = int(input("How many " + extra_item_list[extra_item] + "s would you like?\n"))
    extra_item_total = extra_item_prices[extra_item] * extra_item_amount
    total = total + extra_item_total
    print("Would you like any other food items? (y/n)")
else:
    print("Would you like any food items? (y/n)")

food_item_confirm = input()

food_item_confirm_while = False

if number_of_drinks > 1:
    drinks_suffix = "s"
else:
    drinks_suffix = ""

while food_item_confirm_while == False:
    if food_item_confirm == "y":
        food_item_confirm_while = True
    elif food_item_confirm == "n":
        print("Right then! So your order of " + str(number_of_drinks) + " " + drinks[drink_order] + drinks_suffix + " and one " + extra_item_list[extra_item] + " comes to...")
        payment(total)
    else: 
        print("Looks like you didn't say that right!")

print("Right, you must be hungry! Let me show you the full shop!")

food = extra_item_list + ["toastie", "biscoff", "KitKat", "cheese sandwhich"]
food_prices = extra_item_prices + [4.50, 1.00, 1.00, 3.50]

food_number_track = -1

for item in food:
    food_number_track = food_number_track + 1
    print(str(food_number_track + 1) + ". " + item + " ---> £" + str(food_prices[food_number_track]))

food_choice = int(input("Which number of food would you like?\n"))

food_choice = food_choice - 1

food_amount = int(input("How many " + food[food_choice] + "s would you like?\n"))

food_subtotal = food_prices[food_choice] * food_amount
total = total + food_subtotal

print("\n")

print("Ok - so looking at your order, you have:")
print(str(number_of_drinks) + " " + drinks[drink_order] + drinks_suffix)
if extra_item_amount > 1:
    extra_item_suffix = "s"
else:
    extra_item_suffix = ""
print(str(extra_item_amount) + extra_item_list[extra_item] + extra_item_suffix)
if food_amount > 1:
    food_suffix = "s"
else:
    food_suffix = ""
print("and" + str(food_amount) + food[food_choice] + food_suffix)

payment(total)