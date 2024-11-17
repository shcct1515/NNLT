from datetime import date

d = date.today()
ngay_hien_tai = d.day
thang_hien_tai = d.month
nam_hien_tai = d.year

ho_ten = input("Nhập họ và tên: ")
ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
ngay, thang, nam = map(int, ngay_sinh.split("/"))

tuoi = nam_hien_tai - nam
print(f"{ho_ten}, bạn {tuoi} tuổi.")