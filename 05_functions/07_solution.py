# create a function that accept multiple keywords and show them in key value pair

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name= "shaktiman", power="lazer")
print_kwargs(name= "saad", power="commitment")
print_kwargs(name= "fahad", power="loyality")



