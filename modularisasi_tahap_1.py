"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""
print('\nMenghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung luas segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6
print(f'[Dengan fungsi]\nSegitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas = {hitung_luas_segitiga(alas, tinggi)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(100, 2)}')