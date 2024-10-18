# Nama File: perkalian.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: perkalian dengan rekursif

# DEFINISI DAN SPESIFIKASI
# mul : 2 int > 0 -> int
# mul(x,y) perkalian dengan rekursif

def mul(x,y):
    if y == 0: #basis 0
        return y
    else: # rekurens
        return x + mul(x, y - 1)
    
print(mul(6,5))
print(mul(2,5))
print(mul(6,50))