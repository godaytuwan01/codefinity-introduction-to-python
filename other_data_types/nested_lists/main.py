vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
if "carrots" not in vegetables:
    vegetables.append("carrots")
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
vegetables.sort()
print (f"Updated Vegetable Inventory: {vegetables}")
if "carrots" in vegetables:
    print (f"carrots are already in the list")
if "cucumbers" in vegetables:
    print (f"Cucumbers are already in the list")