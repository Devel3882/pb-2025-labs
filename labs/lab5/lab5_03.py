def primes(a, b):
    result = []
    for i in range(2, b+1):
        if len(result) == 0:
            result.append(i)
        else:
            is_prime = True
            for p in result:
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(i)

    final = []
    for p in result:
        if a <= p <= b:
            final.append(p)

    if final:
        return final
    else:
        return "Error"

print(primes(1, 10))