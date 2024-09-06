# calculate_discount.py

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
