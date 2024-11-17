def giaithua(n):
    #n = int(input("nhap so can tinh: "))
    dapan = 1
    for i in range(1, n+1):
        dapan *= i
    return dapan

def tinhdayso(x, n):
    s = 0
    for i in range(1, n +1):
        s += pow(x, i) / giaithua(i)
    return s