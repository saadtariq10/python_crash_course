file = open ('test.py','w')

try:
    file.write("Chai aur code")

finally:
    file.close()

with open ('test.py','w') as file :
    file.write ("Chai aur code")