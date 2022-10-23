tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)

tuple_d = tuple_a + tuple_b + tuple_c

list1 = []

for item in tuple_d:
    quantity_of_each_item = tuple_d.count(item)
    if quantity_of_each_item <= 1:
        continue
    res1 = (item, quantity_of_each_item)
    list1.append(res1)
res=tuple(list1)

print(res)