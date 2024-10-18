# Nama File   = penanggalan.oy
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 9 September 2024
# Deskripsi   = gak tau 

# DEFINISI DAN SPESIFIKASI 
# max(d,m,y): int,int, int--> int
#   {menentukan nilai maximal dari 2 bilangan }
# dpm(b): int --> int
#   {menentukan nilai maximal dari 2 bilangan }
# is_kabisat(x): int --> int
#   {menentukan nilai maximal dari 2 bilangan }


def is_kabisat(x):
    return (x%4 == 0 and x%100 != 0) or (x // 400 == 0)

def dpm(b):
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 60
    elif b == 4:
        return 91
    elif b == 5:
        return 121
    elif b == 6:
        return 152
    elif b == 7:
        return 182
    elif b == 8:
        return 213
    elif b == 9:
        return 244
    elif b == 10:
        return 274
    elif b == 11:
        return 305
    elif b == 12:
        return 335

def HariKe1900(d,m,y):
    if is_kabisat(y):
        if m > 2:
            return dpm(m) + d + 1 - 1
        else:
            return dpm(m) + d - 1
    else:
        return dpm(m) + d - 1


print(HariKe1900(1, 12,2023))
print(HariKe1900(1, 12,2024))
print(HariKe1900(31, 12,2023))
print(HariKe1900(1, 9,2024))
print(HariKe1900(31, 12,2024))
print(HariKe1900(31, 1,2024))
print(HariKe1900(31, 29,2024))

