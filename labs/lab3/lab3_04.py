num = int(input("Введите число: "))

print(f"Число{' ' if num % 2 == 0 and sum(map(int, list(str(num)))) % 3 == 0 else ' НЕ '}делиться на 6")
