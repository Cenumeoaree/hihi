z = int(input("Introduceti ziua nasterii: "))

l = int(input("Introduceti luna nasterii: "))

a = int(input("Introduceti anul nasterii: "))

s = 0

s += int(z % 10 + z / 10 % 10)

s += int(l % 10 + l / 10 % 10)

s += int(int(a % 10) + int(a / 10 % 10) + int(a / 100 % 10) + int(a / 1000 % 10))


if s < 10:
    print("Cifra destinului este: ", s)
else:
    s += int(int(s % 10) + int(s / 10 % 10) - s)

if s < 10:
    print("Cifra destinului este: ", s)
else:
    s += int(int(s % 10) + int(s / 10 % 10) - s)
    print("Cifra destinului este: ", s)