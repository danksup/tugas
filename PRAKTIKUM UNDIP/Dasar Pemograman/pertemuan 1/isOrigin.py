# Nama File: isOrigin.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 1 Agustus 2024
# Deskripsi: Diberikan sebuah 2 bilangan real, menentukan jika angka tersebut mewakili titik origin

# Definisi dan spesifikasi dari fungsi isOrigin():
# isOrigin() : real, real --> boolean
#   menentukan jika angka tersebut mewakili titik origin


def isOrigin(x,y):
    if x == 0 and y == 0:
        return(print(f'{x},{y} merupakan titik O'))
    else:
        return(print(f'{x},{y} bukan titik origin'))

isOrigin(1,0)
isOrigin(1,1)
isOrigin(0,0)

inputX = input("masukkan titik X: ")
fX = float(inputX)
inputY = input("masukkan titik Y: ")
fY = float(inputY)
isOrigin(fX,fY)

