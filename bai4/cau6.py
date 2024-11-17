import cau5
date = input("nhap ngay thang nam (dd,mm,yyyy): ")
check = date.split(',')
day = int(check[0])
month = int(check[1])
year = int(check[2])

if(month >12 or day >31):
    print("ngay ko phu hop")
elif (cau5.tinhsongaytrongthang(month, year) == False):
    if (day == 31 and month == 12):
        day = 1
        month = 1
        year += 1
        print(f"{day}/{month}/{year}")
    elif(day == 30 and month != 12):
        day = 1
        month +=1
        print(f"{day}/{month}/{year}")
    else:
        day += 1
        print(f"{day}/{month}/{year}")

elif (cau5.tinhsongaytrongthang(month, year) == True):
    if (day == 31 and month ==12):
        day = 1
        month = 1
        year += 1
        print(f"{day}/{month}/{year}")
    elif (day == 31 and month != 12):
        day = 1
        month += 1
        print(f"{day}/{month}/{year}")
    else:
        day += 1
        print(f"{day}/{month}/{year}")

elif (cau5.tinhsongaytrongthang(month, year) == 0):
    if(day == 29):
        day = 1
        month += 1
        print(f"{day}/{month}/{year}")
    else:
        day += 1
        print(f"{day}/{month}/{year}")

elif (cau5.tinhsongaytrongthang(month, year) == 1):
    if(day == 28):
        day = 1
        month += 1
        print(f"{day}/{month}/{year}")
    else:
        day += 1
        print(f"{day}/{month}/{year}") 