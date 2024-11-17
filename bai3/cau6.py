
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

ketqua = []

for i in range(len(list1)):
    ketqua.append(list1[i] + list2[i])

ketqua = " ".join(ketqua)
print(ketqua)
