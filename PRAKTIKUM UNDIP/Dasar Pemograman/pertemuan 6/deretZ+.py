# Nama File: deretZ+.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: menghitung jumlah deret bilangan integer  1 + 2 + 3 + 4 +.... dengan rekursif

# DEFINISI DAN SPESIFIKASI
# s : int > 0 -> int
# s(n) menghitung jumlah deret bilangan integer  1 + 2 + 3 + 4 +.... dengan rekursif

def s(n):
    if n == 0: #basis 0
        return 0
    else: #rekurens
        return n + s(n-1)

print(s(5))
print(s(6))
print(s(1))
print(s(3))