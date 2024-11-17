import re

chuoi = input("Nhập chuỗi ký tự: ")
am = re.findall(r"-\d+", chuoi)

if (am):
    print("Các số nguyên âm:", ", ".join(am))
else:
    print("Không có số nguyên âm trong chuỗi.")