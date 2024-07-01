# write generator function which genrates even numbers upto the limit

def even_generator(limit):
    for i in range(0, limit + 1,2): 
        print(i)

limit = int(input("Enter number to limit even number generation:"))
even_generator(limit)


