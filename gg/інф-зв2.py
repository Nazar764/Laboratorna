n = int(input("Кількість акумуляторів: "))
l = input("Улюблена літера:")

names = []
for i in range(n):
    name = input("=")
    names.append(name)

min = names[0] + l

for name in names:
    mod = name + l
    if mod < min:
        min = mod

print("рядок:", min)