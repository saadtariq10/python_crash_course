# sum of even numbers

limit = int(input("Enter the number up to which you want to sum even numbers: "))

sum_even = 0

for num in range(2, limit + 1, 2):
    sum_even += num

print("Your total sum is:", sum_even)
