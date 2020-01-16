class DK:
    def __init__(self,ho,ten):
        self.ho = ho
        self.ten = ten
    @property
    def ho_va_ten(self):
        return ('{0} {1}'.format(self.ho,self.ten))
    @property
    def emails(self):
        return self.ho + '-' + self.ten + '@dkbike.com'

    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi,ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi

    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None


DKbike = DK('hoang','nam')


DKbike.ho_va_ten = "nguyen bac"

print(DKbike.ho_va_ten)

del DKbike.ho_va_ten

print(DKbike.ho_va_ten)