'''
    Write a Python program named "android-versions" that;
    -takes a double input representing an Android version number
    -uses if-else statements to print the corresponding dessert name.
    -If the input does not match any of these versions,
        print: "Sorry, I don't know this version!"

    Use the following mappings:
        1.5 → Cupcake
        1.6 → Donut
        2.1 → Eclair
        2.2 → Froyo
        2.3 → Gingerbread
        3.1 → Honeycomb
        4.0 → Ice Cream Sandwich
        4.1 → Jelly Bean
        4.4 → KitKat
        5.0 → Lollipop
        8.0 → Oreo
        9.0 → Pie

    *** Use if-else statements to implement the logic! ***
'''

version = float(input("Enter your android version: "))

if version == 1.5:
    print("Cupcake")
elif version == 1.6:
    print("Donut")
elif version == 2.1:
    print("Eclair")
elif version == 2.2:
    print("Froyo")
elif version == 2.3:
    print("Gingerbread")
elif version == 3.1:
    print("Honeycomb")
elif version == 4.0:
    print("Ice Cream Sandwich")
elif version == 4.1:
    print("Jelly Bean")
elif version == 4.4:
    print("KitKat")
elif version == 5.0:
    print("Lollipop")
elif version == 8.0:
    print("Oreo")
elif version == 9.0:
    print("Pie")
else:
    print("Sorry, I don't know this version!")