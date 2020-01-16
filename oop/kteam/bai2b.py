class SieuNhan:
    suc_manh = 50
    def __init__(self,para_ten = "a" ,para_vukhi = "b",para_mau_sac = "c"):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mau_sac
    def xinchao(self):
        print("xin chao ta la: ", self.ten)
        print("suc manh cua ta la: ", self.suc_manh)

    
SieuNhanA = SieuNhan("tien","kiem","blue")
SieuNhanB = SieuNhan("nam","dao","red")

SieuNhanA.xinchao()
SieuNhanB.xinchao()
SieuNhan.xinchao(SieuNhanA)

