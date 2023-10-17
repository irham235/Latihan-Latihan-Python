def mencari_volume_persegi_panjang(panjang,lebar,tinggi):
    """
    Fungsi ini digunakan untuk menghitung volume persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.
        tinggi (int): Tinggi persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    volume_persegi_panjang = panjang * lebar * tinggi
    return volume_persegi_panjang

persegi_panjang_pertama = mencari_volume_persegi_panjang(5,10,3)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_volume_persegi_panjang(4,9,7)
print(persegi_panjang_kedua)
    