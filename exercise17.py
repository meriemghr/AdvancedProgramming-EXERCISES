numbers = []
shoe_sizes = []
for num in [1, 2, 3, 4, 5]:
    numbers.append(num)

numbers.append(3)
numbers.append(4)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

combined_list = numbers + shoe_sizes

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)
print("Combined List:", combined_list)
