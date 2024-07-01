# calculator in a different way

result=0
while True:
    first_num= int(input("Input first number:"))
    second_num= int(input("Input second number:"))
    operator = input("Insert operator (+,-,*,/): ")
    
    if operator == '+':
        result = first_num + second_num
        print("Your sum is ", result)   
    elif operator == '-' :
        result = first_num - second_num
        print("Your difference is ", result)   
    elif operator == '*' :
        result = first_num * second_num
        print("Your product is ", result)   
    elif operator == '/' :
        result = first_num / second_num
        print("Your division is ", result)   
    else:
        print("Wrong operator inserted")
                
    user_response=input("Do you want to attempt another transaction (Y/N): ")
    if user_response=='n':
        break
        

