list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_c = list_a[:]

list_c.extend(list_b)

print(list_c)