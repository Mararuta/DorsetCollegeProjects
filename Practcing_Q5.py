

import json


products = {
    "product_name": "Laptop Bag",
     "price": 35.50,
     "quantity": 8,
     "categories": "Accessories and Bags",
     "Available": True
    }

try:
    with open("product_details.json", "w") as file:
        json.dump(products, file, indent=4)

    with open("product_details.json", "r") as file:
        data = json.load(file)

    data["stock_value"] = data["price"] * data["quantity"]

    with open("product_details.json", "w") as file:
        json.dump(data, file, indent=4)

except Exception as e:
    print("File can not be opened or written to. Error:", e)


print("Product: ", data["product_name"])
print("Price: ", data["price"])
print("Quantity: ", data["quantity"])
print("Stock value: ", data["stock_value"])

                      
