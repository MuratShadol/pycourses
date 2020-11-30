def own(width, length, n=0):
    if width == length:
        print("Длина ребера", length)
        return n + 1
    if width < length:
        print("Длина ребера", width)
        return own(width, length - width, n + 1)
    print("Длина ребера", length)
    return own(width - length, length, n + 1)


a = int(input("width: "))
b = int(input("length: "))
print(own(a, b))
