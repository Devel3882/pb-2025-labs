sesson = int(input("Введите месяц сезона в виде числа: "))

print("Сейчас - ", end="")
if sesson in (1, 2, 12):
    print("зима")
if sesson in (3, 4, 5):
    print("весна")
if sesson in (6, 7, 8):
    print("лето")
if sesson in (9, 10, 11):
    print("осень")
