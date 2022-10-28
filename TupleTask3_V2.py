tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)

tuple_d = tuple_a + tuple_b + tuple_c

result_list = []
list_info = []

for item1 in tuple_d:
    quantity_of_each_item = tuple_d.count(item1)
    if quantity_of_each_item == 1:
        continue
    index = tuple_d.index(item1)
    list_info.append(index)
    for i in range(1, quantity_of_each_item):
        index = tuple_d.index(item1, index + 1)
        list_info.append(index)
    tuple_info = (item1, tuple(list_info))
    list_info.clear()
    if tuple_info in result_list:
        continue
    result_list.append(tuple_info)

res = tuple(result_list)
print(res)