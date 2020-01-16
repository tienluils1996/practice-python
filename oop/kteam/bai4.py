class SieuNhan:
    suc_manh = 50

    def __init__(self, para_ten, para_vukhi, para_mau_sac):
        self.ten = para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mau_sac


class SieuNhanDK(SieuNhan):
    suc_manh = 40

    def __init__(self, para_ten, para_vukhi, para_mau_sac, para_pet):
        # self.ten = para_ten
        # self.vukhi = para_vukhi
        # self.mausac = para_mau_sac
        super().__init__(para_ten, para_vukhi, para_mau_sac)
        self.pet = para_pet


DKbike = SieuNhanDK("tien", "kiem", "blue", "lion")

print(DKbike.__dict__)
print(DKbike.suc_manh)
