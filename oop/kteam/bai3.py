class SieuNhan:
    suc_manh = 50
    def __init__(self,para_ten = "a" ,para_vukhi = "b",para_mau_sac = "c"):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mau_sac
    @classmethod
    def cap_nhat_suc_manh(cls,para_suc_manh):
        cls.suc_manh = para_suc_manh
    @classmethod
    def cap_nhat_suc_manh2(cls,para_suc_manh):
        cls.suc_manh = para_suc_manh

    
SieuNhanA = SieuNhan("tien","kiem","blue")
SieuNhanB = SieuNhan("nam","dao","red")

print(SieuNhan.suc_manh)
print(SieuNhanA.suc_manh)
print(SieuNhanB.suc_manh)

# SieuNhan.cap_nhat_suc_manh(23) # toan bo instance dc cập nhật
# SieuNhanA.cap_nhat_suc_manh(30) # toan bo instance dc cập nhật
SieuNhanA.cap_nhat_suc_manh2(30) # toan bo instance dc cập nhật


print(SieuNhan.suc_manh)
print(SieuNhanA.suc_manh)
print(SieuNhanB.suc_manh)

