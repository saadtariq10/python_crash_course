# Number range between 1 and 10

while True:
    user_input = int(input("Enter a number between 1 and 10:"))
    
    if 0 < user_input < 11:
        print("You entered a valid number:", user_input)
    else:
        print("Invalid number, please enter a number between 1 and 10.")
