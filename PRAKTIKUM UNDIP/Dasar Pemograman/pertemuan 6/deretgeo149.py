# Nama File: deretgeo149.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: menghitung jumlah deret geometri 1 + 4 + 9 +.... dengan rekursif

# DEFINISI DAN SPESIFIKASI
# s : int > 0 -> int
# s(n) menghitung jumlah deret geometri 1 + 4 + 9 +.... dengan rekursif

def s(n):
    if n == 0: #basis 0
        return 0  
    else: #rekurens
        return n**2 + s(n-1)  

print(s(1))
print(s(2))
print(s(3))
print(s(4))
print(s(5))
print(s(6))
print(s(7))
print(s(8))
print(s(10))