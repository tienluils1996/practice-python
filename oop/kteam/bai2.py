class SieuNhan:
    suc_manh = 50
    def __init__(self,para_ten = "a" ,para_vukhi = "b",para_mau_sac = "c"):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mau_sac
    def cap_nhat_suc_manh2(self,para_suc_manh):
        self.suc_manh = para_suc_manh
    
SieuNhanA = SieuNhan("tien","kiem","blue")
SieuNhanB = SieuNhan("tien","kiem","blue")

print(SieuNhan.suc_manh)
print(SieuNhanA.suc_manh)
print(SieuNhanB.suc_manh)

# SieuNhan.suc_manh = 40  # thay doi thuoc tinh bang class.property thi all instance cung bi thay doi theo 
SieuNhanA.suc_manh = 40   # thay doi thuoc tinh bang instance thi chi rieng instance do bi thay doi
SieuNhanB.suc_manh = 10

# SieuNhan.cap_nhat_suc_manh2(30) # thay doi thuoc tinh bang class.method() thi all instance cung bi thay doi theo 
SieuNhanA.cap_nhat_suc_manh2(30) # thay doi thuoc tinh bang instance.method() thi chi rieng instance do bi thay doi
print(SieuNhan.suc_manh)
print(SieuNhanA.suc_manh)
print(SieuNhanB.suc_manh)