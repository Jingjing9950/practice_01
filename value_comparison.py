def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def biggest(a, b, c):
    return bigger(a, bigger(b, c))


def median(a, b, c):
    x = [a, b, c]
    x.remove(biggest(a, b, c))
    return bigger(x[0], x[1])


print(median(9, 3, 6))