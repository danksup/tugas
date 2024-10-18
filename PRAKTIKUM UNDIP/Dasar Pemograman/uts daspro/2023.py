#1
def harga_air(kode,penggunaan):
    if kode == 'A':
        if penggunaan > 10:
            return 30000 + ((penggunaan-10)*2500)
        else:
            return penggunaan*3000
    elif kode == 'B':
        if penggunaan > 10:
            return 40000 + ((penggunaan-10)*3000)
        else:
            return penggunaan*4000
    elif kode == 'C':
        if penggunaan > 10:
            return 50000 + ((penggunaan-10)*3500)
        else:
            return penggunaan*50000
        
print(harga_air('B', 40))
print(harga_air("A", 25))
print(harga_air("A", 2))


#2

def is_kabisat(x):
    return (x % 4 == 0 and x % 100 != 0) or (x // 400 == 0)

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

def HariKe1900(d, m, y):
   if m > 2 and is_kabisat(y):
       return dpm(m) + d + 1 - 1
   else:
       return dpm(m) + d -1

def is_tommorow_friday(d, m, y):
    return (HariKe1900(d, m, y) + 1) % 7 == 5

print(is_tommorow_friday(10,1,1990))
print(is_tommorow_friday(4,1,1990))
print(is_tommorow_friday(15,3,1990))

