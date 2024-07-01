# Duplicate item finder

items = ["apple", "banana", "mango", "apple", "orange"]

unique_item=set()

for item in items:
    if item in unique_item:
        print("Duplicate", item)
    unique_item.add(item)