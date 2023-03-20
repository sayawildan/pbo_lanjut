class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def nakal(self):
        print(self.nama, "nakal")
class anjing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("gog gog!")

kucingA = anjing("doggie", 2, "buldog")
kucingA.nakal() # output: doggie nakal
kucingA.bersuara() # output: gog gog!


#coba yuk

