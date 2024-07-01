# calculator

first_num= int(input("Input first number:"))
second_num= int(input("Input second number:"))
operator = input("Insert operator (+,-,*,/): ")
user_response='y'
result=0;

user_response=input("Do you want to attempt another transaction (Y/N): ")

if user_response=='y':

    while (user_response=='y'):

        if operator == '+':
            result = first_num + second_num
            # print("Your sum is ", result)   
        elif operator == '-' :
            result = first_num - second_num
            # print("Your difference is ", result)   
        elif operator == '*' :
            result = first_num * second_num
            # print("Your product is ", result)   
        elif operator == '/' :
            result = first_num / second_num
            # print("Your division is ", result)   
        else:
            print("Wrong operator inserted")
            
    print("Your result is ", result)           

else:
    print("Thanks for using our product")
            




   

