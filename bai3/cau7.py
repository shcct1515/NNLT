lst = [5, 10, 15, 20, 25, 50, 20]
num = 19

if 20 in lst:
    index = lst.index(20)
    lst[index] = num

print(lst)