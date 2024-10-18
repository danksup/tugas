# Nama File: MO.py
# Pembuat: Agung Rama Pramana Putra
# Tanggal: 31 Agustus 2024
# Deskripsi: Menghasilkan harga rata-rata dari dua di antaraempat buah bilangan tersebut, dengan mengabaikan nilai terbesar dan terkecil

# Definisi dan spesifikasi dari fungsi max2:
# max2 : 2 integer --> integer
#   max2(a,b) menentukan maksimum dari 2 bilangan integer, hanya dengan ekpresi aritmatika: jumlah dari keduan bilangan ditambah dengan selisih kedua bilangan, hasilnya dibagi 2

# Definisi dan spesifikasi dari fungsi min2:
# min2 : 2 integer --> integer
#   max2(a,b) menentukan minimum dari 2 bilangan integer, hanya dengan ekpresi aritmatika: jumlah dari keduan bilangan selisih dengan selisih kedua bilangan, hasilnya dibagi 2

# Definisi dan spesifikasi dari fungsi max4:
# max4 : 4 integer --> integer
#   max4(i,j,k,l) menentukan maksimum dari 4 buah biolangan integer

# Definisi dan spesifikasi dari fungsi min4:
# min4 : 4 integer --> integer
#   min4(i,j,k,l) menentukan minimum dari 4 buah biolangan integer

# Definisi dan spesifikasi dari fungsi MO:
# MO : 4 integer --> real
#   min4(i,j,k,l) menentukan minimum dari 4 buah biolangan integer

def max2(a,b):
    ab = (a + b + abs(a - b)) / 2
    return(ab)

def min2(a,b):
    ab = (a + b - abs(a - b)) / 2
    return(ab)

def max4(i,j,k,l):
    ijkl = max2(max2(i,j), max2(k,l))
    return(ijkl)

def min4(i,j,k,l):
    ijkl = min2(min2(i,j), min(k,l))
    return(ijkl)

def MO(u,v,w,x):
    uvwx = (u + v + w + x - min4(u, v, w ,x) - max(u,v,w,x)) / 2
    return(uvwx)

print(MO(8, 12, 10, 20 ))
