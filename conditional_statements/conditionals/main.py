# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

if product_type == "Fruits" and day_of_week == "Monday":
    print(f"10% discount on Fruits today!")
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print(f"15% discount on Vegetables today!")
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print(f"20% discount on Dairy today!")
elif product_type == "Other":
    print(f"No discount available.")
else:
    print(f"No special discounts today.")