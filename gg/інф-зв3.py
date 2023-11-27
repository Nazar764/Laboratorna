n = int(input())
l = input()
dn = [input() for i in range(n)]


result = max([min([name[:i] + l + name[i:] for i in range(len(name) + 1)]) for name in dn])
print(result)