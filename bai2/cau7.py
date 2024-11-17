import math

def kiem_tra_tam_giac(a, b, c):
    if (a + b > c and a + c > b and b + c > a):
        return True
    return False

def tinh_dien_tich(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (kiem_tra_tam_giac(a, b, c)):
    print("Đây là tam giác hợp lệ.")
    print("Diện tích của tam giác là: ", tinh_dien_tich(a, b, c))
else:
    print("Đây không phải là tam giác hợp lệ.")
