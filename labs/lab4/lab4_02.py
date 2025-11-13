isIputed = False
a = [12, 54, 34, 3, 23]

if isIputed:
    a = list(map(int, input("Введите 5 чисел: ").replace(",", " ").split()))

a = [x**2 for x in a]
print(a)
