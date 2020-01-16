class SieuNhan:
    suc_manh = 50
    def __init__(self,para_ten = "a" ,para_vukhi = "b",para_mau_sac = "c"):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mau_sac
    @staticmethod
    def bien_hinh():
        print("1 2 3 biến hình")

SieuNhanA = SieuNhan("tien","kiem","blue")
SieuNhanB = SieuNhan("nam","dao","red")

SieuNhanA.bien_hinh()
SieuNhan.bien_hinh()


