total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ").strip().lower()

if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    discount = 0.10 
elif day_of_week in ["saturday", "sunday"]:
    discount = 0.20  
else:
    print("Invalid day entered.")
    return

if num_items > 5:
    discount += 0.05 

final_price = total_amount * (1 - discount)

print(f"Total price after discount: {final_price} dinars")
