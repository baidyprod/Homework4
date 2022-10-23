list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_c_a = []
list_c_b = []

for i in list_a:
    if i % 2 == 0:
        list_c_a.append(i)

for i in list_b:
    if i % 2 != 0:
        list_c_b.append(i)

print(list_c_a)
print(list_c_b)
