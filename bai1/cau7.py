import math
a = float(input("nhap so a: "))
b = float(input("nhap so b: "))
c = float(input("nhap so c: "))
delta = pow(b, 2)-4*a*c

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print(f"Phương trình có nghiệm kép: x = {-b / (2*a)}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")