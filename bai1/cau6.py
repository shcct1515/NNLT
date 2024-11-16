name = input("nhap ten cua ban: ")
dic = dict()

for i in name:
    a = name.count(i)
    dic[i] = a

print(f"xin chao{name}")
print(f"ten ban co {dic}")