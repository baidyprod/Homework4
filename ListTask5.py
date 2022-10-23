list_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

res = []

for i in range(10):
    sum = list_c[i] + list_d[i]
    res.append(sum)

print(res)