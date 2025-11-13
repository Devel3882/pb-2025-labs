isIputed = False
a = [12, 54, 34, 3, 23, 54, 66, 12, 3, 3]

if isIputed:
    a = list(map(int, input("Введите 10 чисел: ").replace(",", " ").split()))

a = [(30 if x == 3 else x) for x in a]
print(a)
