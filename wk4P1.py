def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)]) + a[len(b):]
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])]) + b[len(a):]

print(strxor(strxor("20814804c1767293b99f1d9cab3bc3e7".decode("hex"),"Pay Bob 100$"),"Pay Bob 500$").encode("hex"))

