def tinh_toan(chuoi):
    phantu = chuoi.split(",")
    op = []
    
    for pt in phantu:
        if pt.isdigit():
            op.append(float(pt))
        elif pt in ["+", "-", "*", "/"]:
            op.append(pt)
    
    stack = []
    for item in op:
        if isinstance(item, float):
            stack.append(item)
        else:
            b = stack.pop()
            a = stack.pop()
            if item == "+":
                stack.append(a + b)
            elif item == "-":
                stack.append(a - b)
            elif item == "*":
                stack.append(a * b)
            elif item == "/":
                if b == 0:
                    return "Lỗi chia cho 0"
                stack.append(a / b)
    
    if stack:
        return stack[0]
    else:
        return "Biểu thức không hợp lệ"
