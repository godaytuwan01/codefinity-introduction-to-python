# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
def apply_discount (prices):
    discounted_prices = prices.copy()

    for i in range(len(discounted_prices)):
        if discounted_prices[i] > 2.00:
            discounted_prices [i] *= 0.9
            
    return discounted_prices
    
updated_prices = apply_discount(product_prices)
print (f"Updated product prices: ${updated_prices}")