num1 = float(input("nhap so thu nhat: "))
num2 = float(input("nhap so yhu hai: "))
op = input("nhap phep tinh: ")

if(op == '+'):
    print(f"dap an la: {num1+num2}")
elif(op == '-'):
    print(f"dap an la: {num1-num2}")
elif(op == 'x'):
    print(f"dap an la: {num1*num2}")
elif(op == '/'):
    if(num2 == 0):
        print("ko the chia cho 0")
    else:
        print(f"dap an la: {num1+num2}")
else:
    print("phep tinh ko hop le")