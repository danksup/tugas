# Nama File: perkalian3array.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: Menghitung perkalian dengan 3 aray f(n) = 3* n

# DEFINISI DAN SPESIFIKASI
# F : int > 0 -> int
# F(n) Menghitung perkalian dengan 3 aray f(n) = 3* n

def F(n):
    if n == 1: #basis 1
        return 3
    else: #rekurens
        return 3 * F(n-1)
    
print(F(100))