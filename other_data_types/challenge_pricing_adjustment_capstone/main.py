grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99,15),
    "Apples": ("Produce", 1.50, 50)
}
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
   
    print(f"Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        eggs_price - 1,
        grocery_inventory["Eggs"][2],
    )
else:
    print (f"The price of Eggs is reasonable")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        milk_stock + 20  
    )
    print(f"milk needs to be restocked. increasing stock by 20 units.")
    
else:
    print (f"Milk has sufficient stock.")

if grocery_inventory ["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print (f"Apples removed from inventory due to high price.")

print (f"Updated inventory: {grocery_inventory}")