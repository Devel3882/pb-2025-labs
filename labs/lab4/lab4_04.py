tupl = (1, 2, 32, 3, 2)

isOnlyNumbers = True
for x in tupl:
    if type(x) not in [int, float]:
        isOnlyNumbers = False
        break

if isOnlyNumbers:
    print(tuple(sorted(tupl)))
else:
    print(tupl)
