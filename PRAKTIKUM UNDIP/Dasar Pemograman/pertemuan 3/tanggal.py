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

def is_sabtu_lusa(d, m, y):
    return (HariKe1900(d, m, y) + 2) % 7 == 5

print(is_sabtu_lusa(10,1,2024))