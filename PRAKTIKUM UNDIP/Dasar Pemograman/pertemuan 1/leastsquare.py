# Nama File: leastsquare.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 1 Agustus 2024
# Deskripsi: Diberikan sebuah angka, menentukan pangkat2 dari bilangan tersebut

# Definisi dan spesifikasi dari fungsi ls():
# ls() : 4 real --> real
#   menentukan pangkat2 bilangan tersebut

# Definisi dan spesifikasi dari fungsi dif():
# dif() : real --> real
#   menentukan pangkat2 bilangan tersebut

# Definisi dan spesifikasi dari fungsi FX2():
# ls() : real --> real
#   menentukan pangkat2 bilangan tersebut

def FX2(x):
    xx =  x * x
    return(xx)

def dif2(x,y):
    xy =  FX2(x - y)
    return(xy)

def ls(x1,y1,x2,y2):
    xyxy = dif2(y2,y1) + dif2(x2,x1)
    return(xyxy)

print(ls(1,3,5,6))
