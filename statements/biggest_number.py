"""
    Write a Python program that gets 3 numbers from the user and finds the biggest number.
"""

num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))
num3 = int(input("Enter your number 3: "))
biggest = num1

if num1 > num2 and num1 > num3:
    biggest = num1
elif num2 > num1 and num2 > num3:
    biggest = num2
else:
    biggest = num3

print(f"The biggest number is: {biggest}")

#-------------------------------------------

# ~~~~ 2nd way with List Comprehension: ~~~~

# print("enter three numbers:")
# numbers_of_user = [int(input(f"#{i+1}: ")) for i in range(3)]
# print(f"The biggest number is: {max(numbers_of_user)}")
