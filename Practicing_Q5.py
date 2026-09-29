import json

product = {
    "Name": "Laptop Bag",
     "Price": 35.50,
     "Quantity": 8,
     "Categorie": ["Acessories",  "Bags"],
     "Available": True
     }

try:
    with open("product_details.json", "w") as file:
        json.dump(product, file, indent=4)

    with open("product_details.json", "r") as file:
        data = json.load(file)

    print("Product name: ", product["Name"])
    print("Product price: ", product["Price"])
    print("Product quantity: ", product["Quantity"])

    data["stock_value"] = data["Quantity"] * data["Price"]

    with open("product_details.json", "w") as file:
        json.dump(data, file, indent=4)

except FileNotFoundError:
    print("Invalid Json data.")

except Exception as e:
    print("file-handling error.")
