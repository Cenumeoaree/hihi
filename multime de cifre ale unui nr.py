n = int(input("Introduceti un numar natural: "))

v = []

while n > 0:
    a = n % 10
    if a not in v:
        v.append(a)
    n = n // 10

print(v)