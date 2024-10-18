# Nama File: pengurangandanpenambahan.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 3 October 2024
# Deskripsi: pengurangan dan penambahan dengan rekursif

# DEFINISI DAN SPESIFIKASI
# pengurangan :2 int > 0 -> int
# pengurangan(x,y) pengurangan  dengan rekursif

# penambahan :2 int > 0 -> int
# penambahan(x,y) penambahan  dengan rekursif

def pengurangan(x,y):
    if y == 0: #basis 0
        return x
    else: #rekurens
        return (pengurangan(x, y-1) - 1)
    
def penambahan(x,y):
    if y == 0: #basis 0
        return x
    else:
        return penambahan(x, y-1) + 1
    
print(pengurangan(5,4))
print(pengurangan(5,9))
print(pengurangan(20,4))

print(penambahan(5,4))
print(penambahan(5,9))
print(penambahan(20,4))
