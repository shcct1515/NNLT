class con_nguoi:
    def __init__(self, name, cccd, addr, birth):
        self.name = name
        self.cccd = cccd
        self.addr = addr
        self.birth = birth
    def in_thong_tin(self):
        print(f"ten: {self.name}")
        print(f"so cccd: {self.cccd}")
        print(f"dia chi: {self.addr}")
        print(f"ngay sinh: {self.birth}")

class sinh_vien(con_nguoi):
    def __init__(self, name, cccd, addr, birth, mssv, lop, TB, RL):
        super().__init__(name, cccd, addr, birth)
        self.mssv = mssv
        self.lop = lop
        self.TB = TB
        self.RL = RL
    def in_thong_tin(self):
        super().in_thong_tin()
        print(f"MSSV: {self.mssv}")
        print(f"Lop: {self.lop}")
        print(f"Diem trung binh: {self.TB}")
        print(f"Diem ren luyen: {self.RL}")
    def nhap_thong_tin(self, name, cccd, addr, birth, mssv, lop, TB, RL):
        print("thong tin moi vua nhap: ")
        self.name = name
        self.cccd = cccd
        self.addr = addr
        self.birth = birth
        self.mssv = mssv
        self.lop = lop
        self.TB = TB
        self.RL = RL
    def sua_thong_tin(self, name, cccd, addr, birth, lop, TB, RL):
        print("thong tin sau khi cap nhat: ")
        self.name = name
        self.cccd = cccd
        self.addr = addr
        self.birth = birth
        self.lop = lop
        self.TB = TB
        self.RL = RL

sv = sinh_vien("Hien", "093206", "VN", "15/05/2006", "KHDL241020", "KHDL2411", "7,5", "100")
sv.in_thong_tin()

sv.nhap_thong_tin("Hao", "09112", "VN", "31/2/2006", "KHDL2411023", "KHDL2411", "9,0", "100")
sv.in_thong_tin()