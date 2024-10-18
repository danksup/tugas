# Nama File: pangkat.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: pangkat dengan rekursif

# DEFINISI DAN SPESIFIKASI
# pow : 2 int > 0 -> int
# pow(x,y) pangkat dengan rekursif

def pow(x,y):
    if y == 0: #basis 0
        return 1
    else: # rekurens
        return x*pow(x,y-1)
    
print(pow(3,3))
print(pow(2,10))
print(pow(2,5))