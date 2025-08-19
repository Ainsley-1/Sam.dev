

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount (if discount >= 20%) or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price= price - discount_amount
        return final_price
    else:
        return price


def main ():
    
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)
        print(f"The final price after discount is: ${final_price:.2f}")
        
        


    
if __name__ == "__main__":
    main()