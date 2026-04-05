# To print date & time on the bill
from datetime import datetime


# Welcome message
print("------------- LAKSHMI SHIVA GRAND -------------")
print("        Welcome To Lakshmi Shiva Grand")

# Menu for breakfast, lunch, dinner
# Structure: { meal_type: { dish_number: (dish_name, price) } }
Menu = {
    "breakfast": {
        1: ("Idli (2 pcs) Sambar & Chutney", 30),
        2: ("Vada (2 pcs) Sambar & Chutney", 35),
        3: ("Masala Dosa (2 pcs) Sambar & Chutney", 50),
        4: ("Plain Dosa (2 pcs) Sambar & Chutney", 40),
        5: ("Upma with Chutney", 30),
        6: ("Pongal with Sambar & Chutney", 40),
        7: ("Tomato Rice", 40),
        8: ("Palav Rice", 40)
    },
    "lunch": {
        1: ("Full Meals", 80),
        2: ("Curd Rice", 40),
        3: ("Vegetable Biryani with Raita", 90),
        4: ("Paneer Butter Masala", 120),
        5: ("Roti (2 pcs) with Dal", 50),
        6: ("Ragi Mudhe with Full Meals", 100),
        7: ("Tomato Rice", 40),
        8: ("Palav Rice", 40)
    },
    "dinner": {
        1: ("Parotta with Kurma", 60),
        2: ("Chapati with Curry", 50),
        3: ("Fried Rice with Manchurian", 100),
        4: ("Anna With Sambar & Rasam", 70),
        5: ("Ragi Mudhe with Full Meals", 100),
        6: ("Dosa with Chutney & Sambar", 45)
    }
}

# Ask user which menu they want to see
print("Please Select Your Menu :")
print("1. Breakfast")
print("2. Lunch")
print("3. Dinner")

# Take input from user
choice = int(input("Enter Your Choice: "))
if choice == 1:
    meal = "breakfast"
elif choice == 2:
    meal = "lunch"
elif choice == 3:
    meal = "dinner"
else:
    print("Invalid Choice") # Exit if wrong option
    exit()


# Select the chosen meal's dictionary from Menu
Menu = Menu[meal]

# Print the selected meal menu
print(f"\n      --> {meal.capitalize()} Menu <--")
for num, (item, price) in Menu.items():
    print(f"{num} : {item} -- ₹{price}")


# Empty dictionary to store items added to the cart
cart = {}

# allow customer to select multiple dishes
while True:
    dish_num = int(input("\nEnter dish number to buy (press 0 to quit): "))
    if dish_num == 0:  # Exit
        break
    if dish_num in Menu:
        qty = int(input("Enter quantity: "))
        dish_name, dish_price = Menu[dish_num]

        # If dish already in cart, update qty & price
        if dish_name in cart:
            cart[dish_name]['qty'] += qty
            cart[dish_name]['price'] += dish_price * qty
        else:
            cart[dish_name] = {'qty': qty, 'price': dish_price * qty}
        print(f"Added {qty} x {dish_name} to cart.")
    else:
        print("Invalid dish number...")

# Show final bill
print("\n\n===============================================")
print("              LAKSHMI SHIVA GRAND             ")
print("     #123 SIT BACK GATE, Tumkur, Karnataka - 572103")
print("     GSTIN: 36ABCDE1234F1Z5 | Ph: +91 7013553746 ")
print("===============================================")

# Date & Time
now = datetime.now()
print("Date:", now.strftime("%d-%m-%Y"))
print("Time:", now.strftime("%I:%M %p"))
print("===============================================")
print("{:<25} {:<10} {:<10}".format("Item", "Qty", "Price"))
print("-----------------------------------------------")

subtotal = 0
for item, details in cart.items():
    price_each = details['price'] // details['qty']
    print("{:<25} {:<10} {:<10}".format(item, details['qty'], details['price']))
    subtotal += details['price']

# Tax Calculation
tax_rate = 0.05  # 5% GST
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

print("-----------------------------------------------")
print(f"Subtotal:                         ₹{subtotal:.2f}")
print(f"GST (5%):                         ₹{tax_amount:.2f}")
print("-----------------------------------------------")
print(f"Grand Total:                      ₹{grand_total:.2f}")
print("===============================================")
print("   Thank You for Visiting Lakshmi Shiva Grand!    ")
print("   Please Visit Again - Have a Nice Day! 🙏     ")
print("===============================================")
