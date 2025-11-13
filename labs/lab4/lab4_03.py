isIputed = False
debug = False

a = [12, 54, 34, 3, 23]

if isIputed:
    a = list(map(int, input("Введите числа: ").replace(",", " ").split()))

if debug:
    print(max(a), "/", len(a))

print(max(a)/len(a))
