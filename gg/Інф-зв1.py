a, b, c = map(int, input().split(" "))
co = [a, b, c]
co.sort()
min_sum = co[0] + co[1]
print(min_sum)
