def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Example usage:
original_price = 100
discount_percentage = 25
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if final_price == original_price:
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after applying the discount:", final_price)