class SieuNhan:
    def __init__(self,para_ten = "a" ,para_vukhi = "b",para_mau_sac = "c"):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mau_sac
    def xinchao(self):
        print("xin chao, ta chinh la:", self.ten)

SieuNhanA = SieuNhan("tien","kiem","blue")
SieuNhanB = SieuNhan()

print("ten cua sieu nhan la:", SieuNhanA.ten)
print("vu khi cua sieu nhan la:", SieuNhanA.vukhi)
print("mau sac cua sieu nhan la:", SieuNhanB.mausac)
SieuNhanA.xinchao() # instance goi ham
SieuNhanB.xinchao()
# SieuNhan.xinchao() #khong chay dc
SieuNhan.xinchao(SieuNhanA) # cach nay it dung
