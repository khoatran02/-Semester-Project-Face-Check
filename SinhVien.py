class SinhVien:
    def __int__(self,MSSV, HoTen, NhomLop, DiemDanh, path):
        self.MSSV = MSSV
        self.HoTen = HoTen
        self.NhomLop =NhomLop
        self.DiemDanh = DiemDanh
        self.path = path

    def TraMSSV(self):
        return self.MSSV
    def TraPath(self):
        return self.path
