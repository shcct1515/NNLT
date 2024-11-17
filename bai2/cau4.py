def ve_hinh_vuong_rong(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

def ve_tam_giac_tren_trai(n):
    for i in range(n, 0, -1):
        print("* " * i)

print("Hình vuông rỗng:")
ve_hinh_vuong_rong(5)

print("Tam giác vuông góc trên bên trái:")
ve_tam_giac_tren_trai(5)

