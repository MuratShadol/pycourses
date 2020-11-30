def own(width, length, n=0):
    if width == length:
        return n + 1
    if width < length:
        return own(width, length - width, n + 1)
    return own(width - length, length, n + 1)


a = int(input("width: "))
b = int(input("length: "))
print(own(a, b))
