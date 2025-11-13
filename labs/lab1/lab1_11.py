a, b, c = map(float, input("Введите 3 числа (через запятую): ").split(","))

res = (a+c)//b
print(f"({a} + {c}) // {b} = {res}")
