def bank(a, n):
    if a < 30000:
        return "Вклад меньше 30.000"

    ap = min(a // 10000 * 0.3, 5)
    res = 0
    for i in range(1, n+1):
        if i <= 3:      np = 3
        elif 4 <= i <= 6:    np = 5
        else:           np = 2

        _res = a * ((ap + np) / 100)
        res += _res
        a += _res

        #print(res, ap, np, a)
    return res

print(bank(30000, 3))
print(bank(100000, 5))
print(bank(200000, 8))