user_list = []   
while True:
    try:
        user_input = input("Enter a number: ").strip()
        number = int(user_input)

        if number == 0:
            break
          
        user_list.append(number)
        print(f"Current List: {user_list}")
        print(f"Sorted List: {sorted(user_list)}")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Program has ended.")
