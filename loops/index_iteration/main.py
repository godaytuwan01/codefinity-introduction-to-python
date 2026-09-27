prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.1, 0.2, 0.15, 0.05]

for i in range(len(prices)):
    prices[i] = prices[i] * (1 - discount[i])
    print (f"Updated price for item {i}: ${prices[i]:.2f}")