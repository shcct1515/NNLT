import cau4

def tinhsongaytrongthang(month, year):
    #month = int(input("nhap thang: "))
    if(month == 2):
        #year = int(input("nhap nam: "))
        if(cau4.namnhuan(year) == True):
            #print(f"thang {month} co 29 ngay")
            return 0
        else:
            #print(f"thang {month} co 28 ngay")
            return 1
    elif(month <= 7 and month%2 != 0):
        #print(f"thang {month} co 31 ngay")
        return True
    elif(month > 7 and month%2 == 0):
        #print(f"thang {month} co 31 ngay")
        return True
    else:
        #print(f"thang {month} co 30 ngay")
        return False