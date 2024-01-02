# 方案一
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

for x in list1:
    if x in list2:
        print(x, 'in List1 and List2')
    else:
        print(x, 'only in List1')


# 方案二
def compare_lists(list1, list2):
    for data in list1:
        if data in list2:
            print(data, 'in List1 and List2')
        else:
            print(data, 'only in List1')


list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

compare_lists(list1, list2)

