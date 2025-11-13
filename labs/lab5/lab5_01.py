sizes = [
    "s",
    "m",
    "h",
    "d",
    "w",
]
sizes_scale = [
    1,
    1*60,
    1*60*60,
    1*60*60*24,
    1*60*60*24*7,
]

def convert(*args):
    to_convern = args[:-1]
    convert_size = args[-1]
    result = []
    if len(to_convern) > 1:
        for c in to_convern:
            result.append(convert(c, convert_size))
    else:
        a = to_convern[0][:-1]
        b = to_convern[0][-1]
        c = convert_size
        k = sizes_scale[sizes.index(b)] / sizes_scale[sizes.index(c)]
        res = float(a) * k
        if res % 1 == 0: res = int(res)
        return f"{res}{c}"
    return result

print(convert("4h", "5m", "m"))