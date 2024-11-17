import cau1_2

run = True
while(run):
    print("Nhan 1 de tinh chu vi hinh vuong")
    print("Nhan 2 de tinh dien tich hinh vuong")
    print("Nhan 3 de thoat chuong trinh")
    userinput = int(input("nhap su lua chon cua ban: "))

    if(userinput == 1):
        print("ban da chon tinh chu vi")
        a = float(input("nhap do dai canh hinh vuong: "))
        print("dap an la: ", cau1_2.chuvihinhvuong(a))
        input("nhan phim bat ki de quay lai menu")
    elif(userinput == 2):
        print("ban da chon tinh dien tich")
        a = float(input("nhap do dai canh hinh vuong: "))
        print("dap an la: ", cau1_2.dientichhinhvuong)
        input("nhan phim bat ki de quay lai menu")
    elif(userinput == 3):
        print("cam on ban da dung")
        run = False
    else:
        print("su lua chon ko phu hop")
        run = False