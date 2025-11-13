def isIntable(x):
    try:
        int(x)
        return True
    except:
        return False


inp = input("Введите целое число собачих лет для перевода в человеческие: ")

isNum = True
for c in inp:
    if c not in "0123456789":
        isNum = False

# Блок ошибок
if not isNum:
    print("Вы ввели не число")
elif int(inp) < 1:
    print("Вы ввели число меньше 1")
elif int(inp) > 22:
    print("Ошибка :(")

else:
    result = 0
    for i in range(int(inp)):
        if i < 2:
            result += 10.5
        else:
            result += 4
    print(f"Собаке по человечески - {result} лет")