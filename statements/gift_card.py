'''
    Let's say I've got a $100 gift card and you want to buy something in your online store. 
	Write a program that will help me to buy something and display leftover balance after purchase. 

	- If item is not in the list, display message: _**"Invalid item!"**_. 
	- If price is more than $100, display message: _**"Sorry, not enough funds on your gift card!".**_ 

		> **_List of items_**
		> Blanket - 60$
		> Charger - 25$
		> Hat - 25$
		> Headphones - 30$
		> Laptop - 200$
		> Pants - 50$
		> Pillow - 40$
		> Smartphone - 1000$
		> Socks - 5$
		> USB cable - 10$

		Examples: 
		```
		input: Hat

		output: 
            Thank you for your purchase!
            Your current balance is: 75$
		```
'''

balance = 100

items = {"blanket": 60,
         "charger": 25,
         "hat": 25,
         "headphones": 30,
         "laptop": 200,
         "pants": 50,
         "pillow": 40,
         "smartphone": 1000,
         "socks": 5,
         "usb cable": 10}

item_to_buy = input("Enter your item to buy: ").lower()

if item_to_buy not in items:
    print("Invalid item!")
else:
    price = items.get(item_to_buy)
    if price > balance:
        print("Sorry, not enough funds on your gift card!")
    else:
        balance -= price
        print(f"Thank you for your purchase!\nYour current balance is: {balance}$")
