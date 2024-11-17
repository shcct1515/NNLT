import random
run = True
score = 0
wrong = 0

while(run):
    num = random.randint(1, 100)
    print(f"diem cua ban {score}")
    print(f"so lan doan sai {wrong}")
    usernum = int(input("nhap so cua ban: "))

    if(usernum == num):
        score += 1
        print("ban da doan dung")
    elif(usernum != num):
        wrong += 1
        print(f"ban da doan sai so cua may tinh la {num}")
    else:
        print("so ko hop le ban da thua")
        run = False

    if(wrong == 6):
        print("CO HOI CUOI")
    elif(wrong == 7):
        print("NGU")
        run = False