# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
for name, item in inventory.items():
    if item[0] < 30:
        print (f"{name} need restocking.")
    elif item[0] > 100:
        print (f"{name} should be sold at the discounted price of {item[2]}.")
    else:
        print (f"{name} should be sold at the regular price of {item[1]}.")