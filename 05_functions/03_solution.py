# calculate area and circumference from radius

def calculations(radius):
    area = 3.1416 * radius ** 2
    circumference = 2 * 3.1416 * radius
    print("Area:", area , "\nCircumference:", circumference)

print(calculations(13))