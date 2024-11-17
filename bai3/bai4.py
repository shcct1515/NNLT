chuoi = input("Nhập chuỗi ký tự: ")

tong = 0
num = 0

for i in chuoi:
    if i.isdigit():
        tong += int(i)
        num += 1

if num > 0:
    trungbinh = tong / num
    print(f"Tổng là {tong}, trung bình là {trungbinh}.")
else:
    print("Không có số trong chuỗi.")
