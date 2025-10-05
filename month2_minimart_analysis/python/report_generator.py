# Code to generate dictionary summary reports

def generate_sales_report(orders, customers, products):
    #Calculate total products sold
    qty_products_sold = []
    for order in orders:
        qty_products_sold.append(order['quantity'])
    total_products_sold = sum(qty_products_sold)

    #Find most popular product
    product_sales = {}
    for order in orders:
        product_id = order['product_id']
        quantity = order['quantity']
        product_sales[product_id] = product_sales.get(product_id, 0) + quantity

    if product_sales:
        most_popular_id = max(product_sales, key=product_sales.get)
        most_popular_product = products[most_popular_id]['name']
        most_popular_quantity = product_sales[most_popular_id]
    else:
        most_popular_product = "No sales yet"
        most_popular_quantity = 0


    #Calculate revenue per cutomer
    revenue_per_customer = {}
    for order in orders:
        customer_id = order['customer_id']
        product_price = products[order['product_id']]['price']
        order_total = product_price * order['quantity']

        #Apply discount based on customer join date
        from utils import apply_discount
        customer_join_date = customers[customer_id]['join_date']
        final_total = apply_discount(order_total, customer_join_date)

        revenue_per_customer[customer_id] = revenue_per_customer.get(customer_id,0) + final_total

    #Convert customer IDs to names for the report
    revenue_per_customer_named = {}
    for customer_id, revenue in revenue_per_customer.items():
        customer_name = customers[customer_id]['name']
        revenue_per_customer_named[customer_name] = round(revenue, 2)
    
    #Calculate total revenue
    total_revenue = sum(revenue_per_customer.values())

    #Sales by category
    sales_by_category = {}
    for order in orders:
        product_id = order['product_id']
        category = products[product_id]['category']
        quantity = order['quantity']
        sales_by_category[category] = sales_by_category.get(category, 0) + quantity



    #BUILD THE REPORT DICTIONARY
    report = {
        'total_products_sold': total_products_sold,
        'most_popular_product': {
            'name': most_popular_product,
            'quantity_sold': most_popular_quantity
        },
        'revenue_per_customer': revenue_per_customer_named,
        'total_revenue': round(total_revenue, 2),
        'average_order_value': round(total_revenue / len(orders), 2) if orders else 0,
        'total_orders': len(orders),
        'unique_customers': len(revenue_per_customer),
        'sales_by_category': sales_by_category
    }

    return report

def display_report(report):
    print("\n" + "="*60)
    print("📊 MINIMART SALES REPORT")
    print("="*60)
    
    print(f"\n📦 ORDER SUMMARY:")
    print(f"   Total Orders: {report['total_orders']}")
    print(f"   Total Products Sold: {report['total_products_sold']}")
    print(f"   Total Revenue: ${report['total_revenue']:.2f}")
    print(f"   Average Order Value: ${report['average_order_value']:.2f}")
    print(f"   Unique Customers: {report['unique_customers']}")

    print(f"\n🏆 MOST POPULAR PRODUCT:")
    print(f"   {report['most_popular_product']['name']}")
    print(f"   Quantity Sold: {report['most_popular_product']['quantity_sold']}")
    
    print(f"\n💰 REVENUE PER CUSTOMER:")
    for customer, revenue in report['revenue_per_customer'].items():
        print(f"   {customer}: ${revenue:.2f}")
    
    print(f"\n📈 SALES BY CATEGORY:")
    for category, quantity in report['sales_by_category'].items():
        print(f"   {category}: {quantity} units")
    
    print("\n" + "="*60)

def display_large_orders(large_orders, customers, products):
    """Display large orders in a nice format"""
    if not large_orders:
        print("\nNo large orders found.")
        return
    
    print("\n" + "="*50)
    print("🚨 LARGE ORDERS (Over $100)")
    print("="*50)
    
    for order in large_orders:
        customer_name = customers[order['customer_id']]['name']
        product_name = products[order['product_id']]['name']
        
        print(f"Order #{order['order_id']}")
        print(f"   Customer: {customer_name}")
        print(f"   Product: {product_name}")
        print(f"   Quantity: {order['quantity']}")
        print(f"   Total: ${order['total_amount']:.2f}")
        print(f"   {'-'*40}")