# Ticket printer
day = input("Enter the day: ")
age = int(input("Enter the age: "))

if age >= 18:
    price = 12
    if day == "wednesday":
        price -= 2
else:
    price = 8
    if day == "wednesday":
        price -= 2

print(f"The ticket price is ${price}.")
