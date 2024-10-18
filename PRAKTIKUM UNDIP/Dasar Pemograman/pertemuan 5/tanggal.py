# TYPE DATE

# DEFINISI DAN SPESIFIKASI TYPE
# type Hr : integer [1...31]
#   {definisi ini hanya untuk “menamakan” type integer dengan nilai tertentu supaya mewakili hari, 
#   sehingga jika dipunyai suatu nilai integer, kita dapat memeriksa apakah nilai integer tersebut 
#   mewakili Hari yang absah}
# type Bln : integer [1...12]
#   {definisi ini hanya untuk “menamakan” type integer dengan daerah nilai tertentu supaya mewakili bulan}
# type Thn : integer > 0
#   {definisi ini hanya untuk “menamakan” type integer dengan daerah nilai tertentu supaya mewakili tahun}
# type date <d: Hr, m: Bln, y: Thn>
#   {<d,m,y> adalah tanggal d bulan m tahun y}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Day : date -> Hr
#   {Day (D) memberikan hari d dari D yang terdiri dari <d,m,y>}
# Month : date -> Bln
#   {Month (D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
# Year : date -> Thn
#   {Year (D) memberikan tahun y dari D yang terdiri dari <d,m,y>}

# KONSTRUKTOR
# MakeDate : <Hr, Bln, Thn> -> date
#   {MakeDate (<h,b,t>) -> tgl pada hari, bulan, tahun yang bersangkutan}

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
# Nextday : date -> date
#   {NextDay(D): menghitung date yang merupakan keesokan hari dari date D yang diberikan:
#   Nextday (<1,1,80>) adalah (<2,1,80>)
#   Nextday (<31,1,80>) adalah (<1,2,80>)
#   Nextday (<30,4,80>) adalah (<1,5,80>)
#   Nextday (<31,12,80>) adalah (<1,1,81>)
#   Nextday (<28,2,80>) adalah (<29,2,80>)
#   Nextday (<28,2,81>) adalah (<1,3,82>)}

# TYPE DATE (lanjutan)

# Yesterday : date -> date
#   {Yesterday(D): Menghitung date yang merupakan 1 hari sebelum date D yang diberikan:
#   Yesterday (<1,1,80>) adalah <31,12,79>
#   Yesterday (<31,1,80>) adalah <30,1,80>
#   Yesterday (<1,5,80>) adalah <30,4,80>
#   Yesterday (<31,12,80>) adalah <30,12,80>
#   Yesterday (<29,2,80>) adalah <28,2,80>
#   Yesterday (<1,3,80>) adalah <29,2,80>}

# NextNday : date, integer -> date
#   {NextNDay(D,N) : Menghitung date yang merupakan N hari (N adalah nilai integer) sesudah dari date D yang diberikan}

# PREDIKAT
# IsEqD? : 2 date -> boolean
#   {IsEqD?(d1,d2) benar jika d1=d2, mengirimkan true jika d1=d2 and m1=m2 and y1=y2.
#   Contoh : 
#   EqD(<1,1,90>,<1,1,90>) adalah true
#   EqD(<1,2,90>,<1,1,90>) adalah false}
# IsBefore? : 2 date -> boolean
#   {IsBefore?(d1,d2) benar e jika d1 adalah sebelum d2 mengirimkan true jika D1 adalah "sebelum" D2}
# IsAfter? : 2 date -> boolean
#   {IsAfter?(d1,d2) benar jika d1 adalah sesudah d2 mengirimkan true jika D1 adalah "sesudah" D2}
# IsKabisat? : integer -> boolean
#   {IsKabisat?(a) true jika tahun 1900+a adalah tahun kabisat: habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400}

# REALISASI
def hari(d):
    return d[0]

def bulan(m):
    return m[1]

def tahun(y):
    return y[2]

def MakeDate(d, m, y):
    return (d, m, y)

def isKabisat(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def nextNdate(D, N):
    N = N + (hari(D) + (bulan(D) - 1) * 31) + (tahun(D) * 365) + (tahun(D) // 4) - (tahun(D) // 100) + (tahun(D) // 400)
    
    if N > 365:
        return MakeDate(1 + (N - 1) % 31, 1 + ((N - 1) // 31) % 12, tahun(D) + (N - 1) // 365)

    if bulan(D) == 2:
        if isKabisat(tahun(D)):
            if hari(D) + N <= 29:
                return MakeDate(hari(D) + N, bulan(D), tahun(D))
            else:
                return MakeDate(1, 3, tahun(D))
        else:
            if hari(D) + N <= 28:
                return MakeDate(hari(D) + N, bulan(D), tahun(D))
            else:
                return MakeDate(1, 3, tahun(D))
    elif bulan(D) == 4 or bulan(D) == 6 or bulan(D) == 9 or bulan(D) == 11 :
        if hari(D) + N <= 30:
            return MakeDate(hari(D) + N, bulan(D), tahun(D))
        else:
            return MakeDate(1, bulan(D) + 1, tahun(D))
    else:  
        if hari(D) + N <= 31:
            return MakeDate(hari(D) + N, bulan(D), tahun(D))
        else:
            if bulan(D) == 12:
                return MakeDate(1, 1, tahun(D) + 1)
            else:
                return MakeDate(1, bulan(D) + 1, tahun(D))

def Yesterday(D):
    if hari(D) == 1:
        if bulan(D) == 3:
            if isKabisat(tahun(D)):
                return MakeDate(29, 2, tahun(D))
            else:
                return MakeDate(28, 2, tahun(D))
        elif bulan(D) == 5 or bulan(D) == 7 or bulan(D) == 10 or bulan (D)== 12: 
            return MakeDate(30, bulan(D) - 1, tahun(D))
        elif bulan(D) == 1:
            return MakeDate(31, 12, tahun(D) - 1)
        else:
            return MakeDate(31, bulan(D) - 1, tahun(D))
    else:
        return MakeDate(hari(D) - 1, bulan(D), tahun(D))

def isEqD(D1, D2):
    return (hari(D1), bulan(D1), tahun(D1)) == (hari(D2), bulan(D2), tahun(D2))

def isBefore(D1, D2):
    if tahun(D1) != tahun(D2):
        return tahun(D1) < tahun(D2)
    else:
        if bulan(D1) != bulan(D2):
            return bulan(D1) < bulan(D2)
        else:
            return hari(D1) < hari(D2)

def isAfter(D1, D2):
    if tahun(D1) != tahun(D2):
        return tahun(D1) > tahun(D2)
    else:
        if bulan(D1) != bulan(D2):
            return bulan(D1) > bulan(D2)
        else:
            return hari(D1) > hari(D2)

print(f'{'-'*50}NextNdate{'-'*50}')
print(nextNdate((1, 2, 2024), 40))  
print(nextNdate((5, 2, 2024), 40))  
print(nextNdate((1, 4, 2024), 999))  
print(nextNdate((1, 1, 2024), 1000))  

print(f'{'-'*50}isEqD{'-'*50}')
print(isEqD((1, 2, 2024),(5, 2, 2024)))
print(isEqD((1, 2, 2024),(1, 2, 2024)))

print(f'{'-'*50}isBefore{'-'*50}')
print(isBefore((1, 2, 2024),(1, 2, 2024)))
print(isBefore((1, 2, 2024),(3, 2, 2024)))
print(isBefore((1, 2, 2024),(1, 2, 2023)))
print(isBefore((1, 2, 2024),(30, 1, 2024)))
print(isBefore((1, 1, 2024),(1, 2, 2024)))

print(f'{'-'*50}isAfer{'-'*50}')
print(isAfter((1, 2, 2024),(1, 2, 2024)))
print(isAfter((1, 2, 2024),(3, 2, 2024)))
print(isAfter((1, 2, 2024),(1, 2, 2023)))
print(isAfter((1, 2, 2024),(30, 1, 2024)))
print(isAfter((1, 1, 2024),(1, 2, 2024)))

print(f'{'-'*50}yesterday{'-'*50}')
print(Yesterday((1, 1, 1980)))  
print(Yesterday((31, 1, 1980))) 
print(Yesterday((1, 5, 1980)))  
print(Yesterday((31, 12, 1980))) 
print(Yesterday((29, 2, 1980))) 
print(Yesterday((1, 3, 1980)))  