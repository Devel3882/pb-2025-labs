purchases = [
    {"item": "Laptop", "price": 1000, "quantity": 2},
    {"item": "Mouse", "price": 25, "quantity": 5},
    {"item": "Keyboard", "price": 45, "quantity": 3}
]

purchases_total_price = list(map(
    lambda x: {"item": x["item"], "total_price": x["price"] * x["quantity"]},
    purchases
))

sorted_purchases = sorted(purchases_total_price, key=lambda x: x["total_price"])

print(sorted_purchases)