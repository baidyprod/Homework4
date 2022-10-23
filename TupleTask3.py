tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)

tuple_d = tuple_a + tuple_b + tuple_c

result_list = []

for item1 in tuple_d:
    quantity_of_each_item = tuple_d.count(item1)
    if quantity_of_each_item == 1:
        continue
    if quantity_of_each_item == 2:
        index1 = tuple_d.index(item1)
        index2 = tuple_d.index(item1, index1 + 1)
        tuple_info = (item1, (index1, index2))
        if tuple_info in result_list:
            continue
        result_list.append(tuple_info)
    if quantity_of_each_item == 3:
        index1 = tuple_d.index(item1)
        index2 = tuple_d.index(item1, index1 + 1)
        index3 = tuple_d.index(item1, index2 + 1)
        tuple_info = (item1, (index1, index2, index3))
        if tuple_info in result_list:
            continue
        result_list.append(tuple_info)
res = tuple(result_list)
print(res)