# Cat food suggest application

pet = input("Enter the pet type (dog or cat): ")
age = int(input("Enter the age of the pet: "))

if pet == "dog" and age < 2:
    print("Puppy Food")
elif pet == "cat" and age > 5:
    print("Senior Cat Food")
else:
    print("Standard Pet Food")
