# Nama File: pembagian.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: pembagian dengan rekursif

# DEFINISI DAN SPESIFIKASI
# div : 2 int > 0 -> int
# div(x,y) pembagian dengan rekursif

def div(x, y):
    if x < y: #basis kondisional
        return 0  
    else:
        return 1 + div(x - y, y)  

print(div(4, 2))  
print(div(4, 4))  
print(div(10, 2))  
