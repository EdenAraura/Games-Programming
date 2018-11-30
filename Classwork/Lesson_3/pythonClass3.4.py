baby = {'Name': 'Crumble', 'Age': 4, 'Breed': 'Fantastic'}

q = input("What do you want to know about my baby?").lower()

if q == "name":
    print(baby['Name'])
elif q == "age":
    print(baby['Age'])
elif q == "breed":
    print(baby['Breed'])
else:
    print("take this seriously :(")
