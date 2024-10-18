# Nama File: isValid.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 1 Agustus 2024
# Deskripsi: Diberikan sebuah 2 bilangan real, menentukan jika angka tersebut mewakili titik origin

# Definisi dan spesifikasi dari fungsi isOrigin():
# isOrigin() : real, real --> boolean
#   menentukan jika angka tersebut mewakili titik origin


def isValid(x):
    if x < 5 or x > 500:
        return(print("valid"))
    else:
        return(print("tidak valid"))

isValid(5)
isValid(0)
isValid(500)
isValid(6000)

masukan = int(input('masukkan sebuah angka: '))
isValid(masukan)
