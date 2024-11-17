def doc_chu_so(n):
    if n < 0 or n > 99:
        return "Số không hợp lệ"
    
    donvi = {0: "", 1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}
    dacbiet = {10: "mười", 11: "mười một", 12: "mười hai", 13: "mười ba", 14: "mười bốn", 
                15: "mười lăm", 16: "mười sáu", 17: "mười bảy", 18: "mười tám", 19: "mười chín"}
    hangchuc = {2: "hai mươi", 3: "ba mươi", 4: "bốn mươi", 5: "năm mươi", 
                 6: "sáu mươi", 7: "bảy mươi", 8: "tám mươi", 9: "chín mươi"}

    if n < 10:
        return donvi[n]
    elif n in dacbiet:
        return dacbiet[n]
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hangchuc[chuc]
        return f"{hangchuc[chuc]} {donvi[dv]}"
