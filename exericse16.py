numbers = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Enter index (-1 to quit): "))
    except ValueError:
        print("Please enter a valid integer for the index.")
        continue
        
    if index == -1:
        break

    if index < 0 or index >= len(numbers):
        print("Invalid index. Please enter an index between 0 and", len(numbers) - 1)
        continue

    try:
        new_value = int(input("Enter new value: "))
    except ValueError:
        print("Please enter a valid integer for the new value.")
        continue

    numbers[index] = new_value
    print(numbers)numbers = [1, 2, 3, 4, 5]

