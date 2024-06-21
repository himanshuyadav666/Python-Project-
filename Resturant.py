#Define a menu of your Resturant
menu={
    'Pizza':40,
    'Burger':50,
    'Salad':90,
    'coffee':80,
    'pasta':30
}
#Greet
print("Welcome to Python Resturant!")
#Display your menu to custmer
print("\nPizza: Rs40\nBurger: Rs50\nSalad: Rs90\ncoffee: Rs80\nPasta: Rs30")

order_total=0
item_1=input("Enter the name of item you want to order=")
#check item is avliable or not in our resturant
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order!")
else:
    print(f"Order item {item_1} not available yet!")
another_order = input("Do you want to add another item yes/No=")
if another_order == "yes":
    item_2 = input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} is ordered placed!")
    else:
        print(f'your item {order_2} is not available!')
#print total bill
print(f"the total amount of items to pay is {order_total}")