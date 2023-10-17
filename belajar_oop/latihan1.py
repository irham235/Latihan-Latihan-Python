class Mobil:
    # Atribut Instrance
    def __init__(self):
        self.warna = 'Merah'

mobil_1 = Mobil()
print(mobil_1.warna)

mobil_2 = Mobil()
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)