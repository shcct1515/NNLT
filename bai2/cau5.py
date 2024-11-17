from cau1_2 import giaithua

def tinhS(x, n):
    S = x
    for i in range(1, n + 1):
        S += pow(x, (2 * i + 1)) / giaithua(2 * i +1)
    return S

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

print(tinhS(x, n))
