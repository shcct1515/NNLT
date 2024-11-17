chuoi = input("Nhập chuỗi: ")
tukhoa = "Emma"
vitri = chuoi.rfind(tukhoa)

if (vitri != -1):
    print(f"Chuỗi con '{tukhoa}' xuất hiện cuối cùng tại vị trí {vitri}.")
else:
    print(f"Không tìm thấy '{tukhoa}' trong chuỗi.")