# find first non repeating character
input_str="architecture"

for char in input_str:
    if(input_str.count(char)==1):
        print("Char is: ", char)
        break;
    print (char)

