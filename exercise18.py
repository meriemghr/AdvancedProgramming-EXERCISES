def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")
  
numbers = [1, 2, 3, 4, 5]

while True:
    print("\nUpdated List:", numbers)
    display_menu()
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        try:
            value = int(input("Enter value to append: "))
            numbers.append(value)
            print("Updated List:", numbers)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    elif choice == 2:
        try:
            value = int(input("Enter value to insert: "))
            index = int(input("Enter index to insert at: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print("Updated List:", numbers)
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    elif choice == 3:
        try:
            index = int(input("Enter index of element to pop: "))
            if 0 <= index < len(numbers):
                popped_value = numbers.pop(index)
                print(f"Popped value: {popped_value}")
                print("Updated List:", numbers)
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid index. Please enter a valid integer.")

    elif choice == 4:
        try:
            value = int(input("Enter value to remove: "))
            if value in numbers:
                numbers.remove(value)
                print(f"Removed value: {value}")
                print("Updated List:", numbers)
            else:
                print("Value not found in the list.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please choose a valid option from the menu.")
