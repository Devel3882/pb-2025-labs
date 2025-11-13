clients = [
    {"name": "Alice", "income": 50000},
    {"name": "Bob", "income": 120000},
    {"name": "Charlie", "income": 70000}
]

def categorise_incomes(a):
    if a > 100000:
        return "High"
    elif 100000 >= a >= 50000:
        return "Medium"
    else:
        return "Low"

new_clients = list(map(
    lambda x: {"name": x["name"], "income": x["income"], "category": categorise_incomes(x["income"])},
    clients
))

print(new_clients)