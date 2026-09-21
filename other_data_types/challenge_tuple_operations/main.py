# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count ("apples")
print (f"Number of Apples: {apple_count}")

banana_index = shelf.index ("bananas")
print (f"First Banana Index: {banana_index}")

if apple_count < 5:
    print (f"Apples need to be restocked.")
else:
    print (f"Apples are sufficiently stocked.")

if shelf.count ("grapes") == 1:
    print (f"Grapes need to be restocked.")
else:
    print (f"Grapes are sufficiently stocked.")

orange_index = shelf.index ("oranges")
if "oranges" in shelf:
    print (f"Oranges are at index: {orange_index}")
else:
    print (f"Oranges are out of stock.")