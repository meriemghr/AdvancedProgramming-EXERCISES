people = int(input("How many people need a ride? "))
capacity = int(input("How many people fit in one taxi? "))

full_taxis = people // capacity

if people % capacity != 0:
    full_taxis += 1

print("Number of taxis needed:  " + str(full_taxis))
