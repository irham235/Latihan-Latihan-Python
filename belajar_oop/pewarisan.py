class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "Honda", 160)
print(mobil_1.kecepatan)
mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport1 = MobilSport("Hitam", "Ferari", 160)
print(mobil_sport1.kecepatan)
mobil_sport1.turbo()
print(mobil_sport1.kecepatan)