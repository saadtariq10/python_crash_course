# Count positive numbers

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count = positive_number_count + num

print("Total Positive numbers are: " + str(positive_number_count))
