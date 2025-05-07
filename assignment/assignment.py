# Input
food_id = int(input("Enter Food ID: "))  # int
food_name = input("Enter Food Name: ")  # str
price = float(input("Enter Price: "))  # float
categories = input("Enter Categories (comma-separated): ").split(",")  # list
ingredients = set(input("Enter the ingredients: ").split(","))  # set
store_open_or_not = input("Enter store open or not:(True/False): ").lower() == "true"  # bool
supplier_details = {
    "restaurant_name": input("Enter the restaurant name: "),
    "restaurant_contact": int(input("Enter the number: "))
}  # dict
restaurant_address = tuple(input("Enter the address (comma-separated): ").split(","))  # tuple

# Output Formats

print("\n1. Using Comma Separation (sep=',')")
print("Food ID, Name, Price, categories, store_open_or_not, ingredients, supplier_details, restaurant_address",
      food_id, food_name, price, categories, store_open_or_not, ingredients, supplier_details, restaurant_address, sep=", ")

print("\n2. Using Percentage Formatting (% operator)")
print("Food Price: ₹%.2f" % price)
print("Supplier Contact: %d" % supplier_details["restaurant_contact"])

print("\n3. Using f-strings")
print(f"Food Name: {food_name}")
print(f"Price: ₹{price}")
print(f"Store Open: {store_open_or_not}")
print(f"Categories: {categories}")
print(f"Ingredients: {ingredients}")
print(f"Restaurant: {supplier_details['restaurant_name']} ({supplier_details['restaurant_contact']})")
print(f"Address: {restaurant_address}")

print("\n4. Using .format() method")
print("Food ID: {}, Name: {}, Price: ₹{}".format(food_id, food_name, price))
print("Restaurant: {} | Contact: {}".format(
    supplier_details["restaurant_name"], supplier_details["restaurant_contact"]))

# Safe way to print address
print("Address: {}".format(", ".join(restaurant_address)))
