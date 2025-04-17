product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
categories_input = input("Enter Categories (comma-separated): ")
categories = [cat.strip() for cat in categories_input.split(',')]
available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)
discount = float(input("Enter Discount Percentage: "))
features_input = input("Enter Product Features (comma-separated): ")
product_features = set(feature.strip() for feature in features_input.split(','))
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

