# Nama File: isAnA.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 1 Agustus 2024
# Deskripsi: Diberikan sebuah string, menentukan jika angka tersebut A atau bukan A

# Definisi dan spesifikasi dari fungsi isAnA:
# isAnA() : string --> boolean
#   menentukan jika bilangan yang diberikan adalah A atau bukan A


def isAnA(c):
    if c == 'A':
        benarA = 'karakter tesebut benar A'
        return(print(benarA))
    else:
        bukanA = f'{c} bukan A'
        return(print(bukanA))

isAnA(1)
isAnA(0)
isAnA(-1)
isAnA('A')

masukan = input("masukkan sesuatu: ")
isAnA(masukan)


