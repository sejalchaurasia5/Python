#defibe the menu of restuarant
menu = {
    'Pizza':40,
    'pasta':50,
    'burger':25,
    'salad':45,
    'coffee':80,
}

#Greets
print("Welcome to PYTHON Restuarant")
print("Pizza: rs40\npasta: rs50\nBurger: rs25\nsalad: rs45\ncoffee: rs80")

order_total = 0


item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print( f"Please order something that we can serve you")    

another_order = input("Do you want to add another item?  (Yes/No) ")    
if another_order == "Yes":
    item_2 = input ("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print( f"Ordered item {item_2} is not available!")
    else:
        print(f"ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")            