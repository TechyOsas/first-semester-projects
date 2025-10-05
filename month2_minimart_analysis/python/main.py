# Entry point for the MiniMart data reporting system

from utils import *
from report_generator import *

customers = {}
products = {}
orders = []
next_customer_id = 1
next_product_id = 101
next_order_id = 1001

def add_customer():
    global next_customer_id
    print("\n--- Add New Customer ---")
    
    # Get customer name with validation
    while True:
        name = input("Enter customer name: ").strip()
        is_valid, message = validate_name(name)
        if is_valid:
            break
        print(f"Error: {message}")
    
     # Get customer email
    email = input("Enter customer email: ").strip()


    # Create customer record
    customer = {
        'customer_id': next_customer_id,
        'name': name,
        'email': email,
        'join_date': '2025-01-15'
    }
    
    customers[next_customer_id] = customer
    print(f"✅ Customer '{name}' added successfully! (ID: {next_customer_id})")
    next_customer_id += 1

def add_product():
    """Add a new product to the system"""
    global next_product_id
    
    print("\n--- Add New Product ---")
    
    # Get product name
    name = input("Enter product name: ").strip()
    
    # Get product category
    category = input("Enter product category: ").strip()
    
    # Get product price with validation
    while True:
        price_str = input("Enter product price: $").strip()
        is_valid, message = validate_price(price_str)
        if is_valid:
            price = float(price_str)
            break
        print(f"Error: {message}")
    
    product = {
        'product_id': next_product_id,
        'name': name,
        'category': category,
        'price': price
    }
    
    products[next_product_id] = product
    print(f"✅ Product '{name}' added successfully! (ID: {next_product_id})")
    next_product_id += 1


def add_order():
    """Add a new order to the system"""
    global next_order_id
    
    print("\n--- Add New Order ---")
    
    # Show available customers
    if not customers:
        print("No customers available. Please add customers first.")
        return
    
    print("\nAvailable Customers:")
    for customer_id, customer in customers.items():
        print(f"  {customer_id}: {customer['name']}")

    # Get customer ID
    while True:
        try:
            customer_id = int(input("\nEnter customer ID: "))
            if customer_id in customers:
                break
            else:
                print("Error: Customer ID not found.")
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # Show available products
    if not products:
        print("No products available. Please add products first.")
        return
    
    print("\nAvailable Products:")
    for product_id, product in products.items():
        print(f"  {product_id}: {product['name']} - ${product['price']:.2f}")

    # Get product ID
    while True:
        try:
            product_id = int(input("\nEnter product ID: "))
            if product_id in products:
                break
            else:
                print("Error: Product ID not found.")
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # Get quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            else:
                print("Error: Quantity must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid number.")

     # Create order record
    order = {
        'order_id': next_order_id,
        'customer_id': customer_id,
        'product_id': product_id,
        'quantity': quantity
    }
    
    orders.append(order)

    # Calculate order total
    product_price = products[product_id]['price']
    order_total = product_price * quantity
    customer_name = customers[customer_id]['name']
    product_name = products[product_id]['name']
    
    print(f"✅ Order #{next_order_id} added successfully!")
    print(f"   Customer: {customer_name}")
    print(f"   Product: {product_name}")
    print(f"   Quantity: {quantity}")
    print(f"   Total: ${order_total:.2f}")
    
    next_order_id += 1

def view_customers():
    """Display all customers"""
    print("\n--- All Customers ---")
    if not customers:
        print("No customers found.")
        return
    
    for customer_id, customer in customers.items():
        print(f"ID: {customer_id}, Name: {customer['name']}, Email: {customer['email']}")

def view_products():
    """Display all products"""
    print("\n--- All Products ---")
    if not products:
        print("No products found.")
        return
    
    for product_id, product in products.items():
        print(f"ID: {product_id}, Name: {product['name']}, Category: {product['category']}, Price: ${product['price']:.2f}")

def view_orders():
    """Display all orders"""
    print("\n--- All Orders ---")
    if not orders:
        print("No orders found.")
        return
    
    for order in orders:
        customer_name = customers[order['customer_id']]['name']
        product_name = products[order['product_id']]['name']
        product_price = products[order['product_id']]['price']
        order_total = product_price * order['quantity']
        
        print(f"Order #{order['order_id']}: {customer_name} bought {order['quantity']} x {product_name} = ${order_total:.2f}")


def currency_converter_tool():
    """Simple currency converter tool"""
    print("\n--- Currency Converter ---")
    
    if not products:
        print("No products available. Please add products first.")
        return
    
    print("\nAvailable Products:")
    for product_id, product in products.items():
        print(f"  {product_id}: {product['name']} - ${product['price']:.2f}")

    # Get product to convert
    while True:
        try:
            product_id = int(input("\nEnter product ID to convert: "))
            if product_id in products:
                break
            else:
                print("Error: Product ID not found.")
        except ValueError:
            print("Error: Please enter a valid number.")
    
    product_price = products[product_id]['price']
    
    print(f"\nProduct: {products[product_id]['name']}")
    print(f"Price in USD: ${product_price:.2f}")
    print("\nConverted Prices:")
    print(f"  NGN (Nigerian Naira): ₦{convert_currency(product_price, 'NGN'):.2f}")
    print(f"  EUR (Euro): €{convert_currency(product_price, 'EUR'):.2f}")
    print(f"  GBP (British Pound): £{convert_currency(product_price, 'GBP'):.2f}")
    print(f"  JPY (Japanese Yen): ¥{convert_currency(product_price, 'JPY'):.0f}")
    print(f"  CAD (Canadian Dollar): ${convert_currency(product_price, 'CAD'):.2f} CAD")

def add_sample_data():
    """Add some sample data for testing"""
    global customers, products, orders, next_customer_id, next_product_id, next_order_id
    
    # Sample customers
    customers[1] = {
        'customer_id': 1,
        'name': 'John Doe',
        'email': 'john@email.com',
        'join_date': '2024-01-15'
    }
    customers[2] = {
        'customer_id': 2, 
        'name': 'Jane Smith',
        'email': 'jane@email.com',
        'join_date': '2024-01-10'
    }
    next_customer_id = 3

    # Sample products
    products[101] = {
        'product_id': 101,
        'name': 'Milk',
        'category': 'Dairy',
        'price': 3.99
    }
    products[102] = {
        'product_id': 102,
        'name': 'Bread', 
        'category': 'Bakery',
        'price': 2.49
    }
    products[103] = {
        'product_id': 103,
        'name': 'Eggs',
        'category': 'Dairy', 
        'price': 4.99
    }
    next_product_id = 104


    # Sample orders
    orders.append({
        'order_id': 1001,
        'customer_id': 1,
        'product_id': 101,
        'quantity': 2
    })
    orders.append({
        'order_id': 1002,
        'customer_id': 2,
        'product_id': 102,
        'quantity': 3
    })
    orders.append({
        'order_id': 1003,
        'customer_id': 1,
        'product_id': 103,
        'quantity': 1
    })
    next_order_id = 1004


"""Main program loop"""
print("🚀 Welcome to Minimart Data Reporting System!")
add_sample_data()
while True:
    print("="*50)
    print("1. Add Customer")
    print("2. Add Product") 
    print("3. Add Order")
    print("4. View Customers")
    print("5. View Products")
    print("6. View Orders")
    print("7. Generate Sales Report")
    print("8. View Large Orders")
    print("9. Currency Converter")
    print("10. Exit")
    print("="*50)

    choice = input("Enter your choice (1-10): ").strip()
    
    if choice == '1':
        add_customer()
    elif choice == '2':
        add_product()
    elif choice == '3':
        add_order()
    elif choice == '4':
        view_customers()
    elif choice == '5':
        view_products()
    elif choice == '6':
        view_orders()
    elif choice == '7':
        if orders:
            report = generate_sales_report(orders, customers, products)
            display_report(report)
        else:
            print("\nNo orders available to generate report.")
    elif choice == '8':
        large_orders = flag_large_orders(orders, products)
        display_large_orders(large_orders, customers, products)
    elif choice == '9':
        currency_converter_tool()
    elif choice == '10':
        print("\nThank you for using Minimart Data Reporting System! Goodbye! 👋")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1-10.")