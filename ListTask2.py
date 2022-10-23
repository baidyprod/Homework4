list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_c = []

for i in range(5):
    list_c.append(list_a[i])
    list_c.append(list_b[i])
print(list_c)