def kiem_tra_ngoac(chuoi):
    list = []
    ngoac = {"{": "}", "[": "]", "(": ")"}
    for ky_tu in chuoi:
        if ky_tu in ngoac:
            list.append(ky_tu)
        elif ky_tu in ngoac.values():
            if not list or ngoac[list.pop()] != ky_tu:
                return False
    return len(list) == 0

chuoi = input("Nhập chuỗi chứa dấu ngoặc: ")
if kiem_tra_ngoac(chuoi):
    print("Các dấu ngoặc đã mở và đóng đủ.")
else:
    print("Các dấu ngoặc không đúng.")