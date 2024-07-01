# write  function to calculate sum of numbers

def square_calculation(user_input):
    square=user_input**2
    print("Square of", user_input, "is", square)


user_input=int(input("Please enter a number to get its square: "))
square_calculation(user_input)
