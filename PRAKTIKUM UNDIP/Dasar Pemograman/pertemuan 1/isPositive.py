# Nama File: isPositive.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 31 Agustus 2024
# Deskripsi: Diberikan sebuah angka, menentukan jika angka tersebut positif atau tidak positif

# Definisi dan spesifikasi dari fungsi isPositive:
# isPositive() : integer --> boolean
#   menentukan jika bilangan yang diberikan positif atau tidak


def isPositive(angka):
    if angka > 0:
        positif = f'{angka} merupakan bilangan positif'
        return(print(positif))
    else:
        negatif = f'{angka} bukanlah angka positif'
        return(print(negatif))

isPositive(0)
isPositive(1)
isPositive(-1)

input_angka = input('masukkan angka: ')
try:
    val = int(input_angka)
    isPositive(val)
except ValueError:
    print("hanya masukkan angka")
