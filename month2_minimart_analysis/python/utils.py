# Utility functions for data conversion and filtering

def convert_currency(amount_usd, target_currency):
    #This converts USD to other currencies
    exchange_rates = {
        'NGN': 1471.85, #Nigerian Naira
        'EUR': 0.85, #Euro
        'GBP': 0.74, #British Pound
        'JPY': 147.44, #Japanese Yen
        'CAD': 1.40 #Canadian Dollar
    }

    if target_currency in exchange_rates:
        return amount_usd * exchange_rates[target_currency]
    else:
        return amount_usd


def flag_large_orders(orders, products):
    large_orders = []
    threshold = 100

    for order in orders:
        product_price = products[order['product_id']]['price']
        order_total = product_price * order['quantity']

        if order_total > threshold:
            large_orders.append({
                'order_id': order['order_id'],
                'customer_id': order['customer_id'],
                'product_id': order['product_id'],
                'quantity': order['quantity'],
                'total_amount': order_total
            })

    return large_orders

def apply_discount(original_price, customer_join_date):
    #Apply discounts based on how long the customer has been patronizing the company.
    from datetime import datetime

    join_date = datetime.strptime(customer_join_date, "%Y-%m-%d")
    days_since_join = (datetime.now() - join_date).days

    discount = 0.0

    #Loyalty discount
    if days_since_join > 180: #more than 6 months
        discount += 0.10

    #Bulk discount
    if original_price > 200:
        discount += 0.15
    elif original_price > 100:
        discount += 0.10
    elif original_price > 50:
        discount += 0.05

    #Cap discount at 25%
    discount = min(discount, 0.25)

    return original_price * (1 - discount)


def validate_name(name):
    if not name.replace(" ", "").isalpha():
        return False, "Name should contain only letters and spaces"
    
    if len(name.strip()) < 2:
        return False, "Name should be at least 2 characters long"
    
    return True, "Valid name"

def validate_age(age_str):
    age = int(age_str)
    if 5 <= age <= 120:
        return True, "Valid age"
    else:
        return False, "Age should be between 5 and 120"
    
def validate_price(price_str):
    price = float(price_str)
    if price > 0:
        return True, "Valid price"
    else:
        return False, "Price must be greater than 0"