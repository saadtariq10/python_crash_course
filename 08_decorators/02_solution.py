




def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(args) for arg in args)
        kwargs_value = ', '.join(f"{k},{v}" for k,v in kwargs)
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello "):
    print(f"{greeting}, {name}")

greet("Najaf", "Hello there!")


@debug
def hello():
    print("Hello, world!")






