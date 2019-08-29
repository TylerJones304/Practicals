# Number of items: 3
# Price of item: 100
# Price of item: 35.56
# Price of item: 3.24
# Total price for 3 items is $124.92

number_of_items = int(input("Please the amount of items bought: "))
price_of_items = 0
total_items = 0
for i in range(number_of_items):
    price_of_items = float(input("Please enter price of item"))
    total_items += price_of_items

while price_of_items <0:
    print("Invalid number")
    number_of_items = int(input("Please the amount of items bought: "))

if total_items > 100:
    total_items = total_items * 0.9

print("The total price for", number_of_items, "items is $", total_items, )