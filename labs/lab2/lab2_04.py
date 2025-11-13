num = int(input("Введите число для которого хотите факторил: "))

result = 1
for i in range(2, num+1):
    result *= i

print(result)