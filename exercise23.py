while True:
    try:
        N = int(input("Please enter a positive integer: "))
        if N <= 0:
            print("The number must be positive. Please try again.")
            continue
        break 
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(-N, N + 1):
    if i != 0:
        print(i, end=" ")
