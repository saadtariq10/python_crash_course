# Number guessing game
import random
max_attempt = 0
user_input = 0
random_num= random.randint(0,20);
while (max_attempt < 5):
    max_attempt=max_attempt+1
    user_input=int(input("Guess number between 0 and 20:"))  
    if user_input == random_num :
        print("Congratulations! You have guessed the number correctly")
        break
    elif user_input > random_num :
        print("Your guess is too high")
    else :
        print("Your guess is too low")