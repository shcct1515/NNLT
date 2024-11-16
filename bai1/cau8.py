string = input("nhap chuoi cua ban: ")
chuhoa = ""
chuthuong = ""

for i in string:
    if(i.isupper()):
        chuhoa += i
    elif(i.islower()):
        chuthuong += i
print(chuthuong+chuhoa)