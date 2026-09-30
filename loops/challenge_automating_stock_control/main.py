# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

for product in inventory.values():
    while product[0] < product[1]:
        product[0] += product[2]
    if product[0] > discount_threshold and not product[3]:
        product[3] = True
print (inventory)