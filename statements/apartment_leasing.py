'''
Write a Python program that calculates the starting rent based on the number of bedrooms
a customer is interested in.

Requirements:
    -Print a welcome message: "Welcome to NullPointer Apartments!"
	-Ask the user for the number of bedrooms they want using an integer input: "Number of bedrooms you are interested:"
	-Use if-elif-else statements to print the selection and the price based on these rules:

		1 Bedroom: Print "One Bedroom Selected" and "Starting Price: 1100"
		2 Bedrooms: Print "Two Bedroom Selected" and "Starting Price: 1850"
		3 Bedrooms: Print "Three Bedroom Selected" and "Starting Price: 2550"
	    Any other number: Print "No such Bedrooms available"

Note: Ensure your output matches the format exactly (including new lines if you prefer, or separate print statements).
'''

print("Welcome to NullPointer Apartments!")

user_input = int(input("Number of bedrooms you are interested: "))
one_bedroom_price = 1100
two_bedroom_price = 1850
three_bedroom_price = 2550

if user_input == 1:
    print(f"One Bedroom Selected\nStarting Price: {one_bedroom_price}")
elif user_input == 2:
    print(f"Two Bedroom Selected\nStarting Price: {two_bedroom_price}")
elif user_input == 3:
    print(f"Three Bedroom Selected\nStarting Price: {three_bedroom_price}")
else:
    print("No such Bedrooms available")
