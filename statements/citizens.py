'''
Task:
Write a Python program that tracks the count of senior and non-senior citizens based on age.
Requirements:
    1.Inputs:
        Ask for the current counts: "Enter current count for seniorCitizens and nonSeniorCitizens:" (Take two integer inputs).
        Ask for the new citizen's age: "What is new citizen's age?"
    2.Logic:
        If the age is 65 or older, print "Senior Citizen" and increment the senior count by 1.
        Otherwise, print "Non-Senior Citizen" and increment the non-senior count by 1.
    3.Output:
        Print the updated counts:
        "New seniorCitizens count [count]"
        "New nonSeniorCitizens count [count]"`
'''

senior_citizens = int(input("Enter current count for senior citizens: "))
non_senior_citizens = int(input("Enter current count for non-senior citizens: "))
new_citizen_age = int(input("What is new citizen's age?: "))

if new_citizen_age <= 0:
    print("Invalid age!")
else:
    if 0 < new_citizen_age <= 65:
        non_senior_citizens += 1
    elif new_citizen_age > 65:
        senior_citizens += 1
        
    print(f"New senior citizens count: {senior_citizens}")
    print(f"New non-senior citizens count {non_senior_citizens}")

        


