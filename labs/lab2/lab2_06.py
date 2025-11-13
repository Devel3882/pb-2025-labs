num = int(input("Введите номер числа из последовательности фибоначии: "))

print("0\t| 0")
a1, a2 = 0, 1
for i in range(num):
    print(f"{i+1}\t| {a2}")
    a1, a2 = a2, a1+a2



"""if num == 0:
    print(0)
else:
    print(a2)"""