class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("Honda")
mobil_1.intro_mobil()