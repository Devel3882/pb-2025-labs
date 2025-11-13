dictionary = {
    "Banana": 3.99,
    "Apple": 2.4,
    "Bomb": 300,
}

maxCostHas = max(dictionary, key=lambda x: dictionary[x])
minCostHas = min(dictionary, key=lambda x: dictionary[x])

print(f"Максимальная цена у товара {maxCostHas} с ценой {dictionary[maxCostHas]}")
print(f"Минимальная цена у товара {minCostHas} с ценой {dictionary[minCostHas]}")