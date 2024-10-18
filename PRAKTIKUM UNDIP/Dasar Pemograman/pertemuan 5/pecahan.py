# Nama File   = pecahan.py
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 29 September 2024
# Deskripsi   = Didefinisikan suatu type bernama Pecahan, yang terdiri dari pembilang dan penyebut.

#DEFINISI DAN SPESIFIKASI TYPE
# type pecahan: <n:int >=0; integer >0>
#   {<n:int >=0; integer >0> n adalah pembilang (numerator) dan d adalah penyebut (denumerator). Penyebut sebuah Pecahan tidak boleh 0}

#DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# pembilang : pecahan -> integer >=0
#   {pembilang(x) memberikan numerator pembilang n dari pecahan tersebut}
# penyebut : pecahan -> integer >0
#   {penyebut(x) memberikan denumerator pembilang n dari pecahan tersebut}

#DEFINISI DAN SPESIFIKASI KONTRUKTOR
# MakePecahan : integer >=0, integer > 0 -> pecahan
#   {MakePecahan(x,y) membentuk seuah pecahan dari pembilang x dan penyebut y, dengan x dan y integer}

#DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN
#   { Operator aritmatika Pecahan }
# AddP : 2 pecahan → pecahan
#   { AddP(P1, P2) : Menambahkan dua buah pecahan P1 dan P2 : n1/d1 + n2/d2 = (n1 * d2 + n2 * d1) / d1 * d2 }
# SubP : 2 pecahan → pecahan
#   { SubP(P1, P2) : Mengurangkan dua buah pecahan P1 dan P2 Mengurangkan dua pecahan : n1/d1 - n2/d2 = (n1 * d2 - n2 * d1) / d1 * d2 }
# MulP : 2 pecahan → pecahan
#   { MulP(P1, P2) : Mengalikan dua buah pecahan P1 dan P2 Mengalikan dua pecahan : n1/d1 * n2/d2 = n1 * n2 / d1 * d2 }
# DivP : 2 pecahan → pecahan
#   { DivP(P1, P2) : Membagi dua buah pecahan P1 dan P2 Membagi dua pecahan : (n1/d1) / (n2/d2) = n1 * d2 / d1 * n2 }
# RealP : pecahan → real
#   { Menuliskan bilangan pecahan dalam notasi desimal }

#DEFINISI DAN SPESIFIKASI PREDIKAT
# { Operator relasional Pecahan }
# IsEqP? : 2 pecahan → boolean
#    { IsEqP?(p1, p2) true jika p1 = p2 Membandingkan apakah dua buah pecahan samailainya: n1/d1 = n2/d2 jika dan hanya jika n1d2 = n2d1 }
# IsLtP? : 2 pecahan → boolean
#   { IsLtP?(p1, p2) true jika p1 < p2 Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 < n2/d2 jika dan hanya jika n1d2 < n2d1 }
# IsGtP? : 2 pecahan → boolean
#   { IsGtP?(p1, p2) true jika p1 > p2 Membandingkan nilai dua buah pecahan, apakah p1 lebih besar nilainya dari p2: n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1 }


#REALISASI
def pembilang(x):
    return int(x[0])
def penyebut(x):
    return int(x[4])
def MakePecahan(x, y):
    return f"{x}\n—\n{y}"

def AddP(p1, p2):
    return MakePecahan((pembilang(p1)* penyebut(p2) + pembilang(p2)*penyebut(p1)),(penyebut(p1)*penyebut(p2)))
def SubP(p1, p2):
    return MakePecahan((pembilang(p1)* penyebut(p2) - pembilang(p2)*penyebut(p1)),(penyebut(p1)*penyebut(p2)))
def MulP(p1, p2):
    return MakePecahan((pembilang(p1)*pembilang(p2)),(penyebut(p1)*(penyebut(p2))))
def DivP(p1, p2):
    return MakePecahan((pembilang(p1)*penyebut(p2)),(penyebut(p1)*(pembilang(p2))))
def RealP(x):
    pembilang(x) / penyebut(x)

def IsEqP(p1,p2):
    return pembilang(p1)*penyebut(p2) == penyebut(p1)*pembilang(p2)
def IsLtP(p1,p2):
    return pembilang(p1)*penyebut(p2) < penyebut(p1)*pembilang(p2)
def IsGtP(p1,p2):
    return pembilang(p1)*penyebut(p2) > penyebut(p1)*pembilang(p2)


print(f'{'-'*50}AddP{'-'*50}')
print(AddP(MakePecahan(1,2), MakePecahan(1,2)))
print(f'{'-'*50}SubP{'-'*50}')
print(SubP(MakePecahan(1,2), MakePecahan(1,2)))
print(f'{'-'*50}MulP{'-'*50}')
print(MulP(MakePecahan(1,2), MakePecahan(1,2)))
print(f'{'-'*50}DivP{'-'*50}')
print(DivP(MakePecahan(1,2), MakePecahan(1,2)))

print(f'{'-'*50}IsEqP{'-'*50}')
print(IsEqP(MakePecahan(1,2), MakePecahan(1,2)))
print(IsEqP(MakePecahan(1,2), MakePecahan(3,3)))
print(IsEqP(MakePecahan(3,3), MakePecahan(1,2)))

print(f'{'-'*50}IsGtP{'-'*50}')
print(IsGtP(MakePecahan(1,2), MakePecahan(1,2)))
print(IsGtP(MakePecahan(1,2), MakePecahan(3,3)))
print(IsGtP(MakePecahan(3,3), MakePecahan(1,2)))

print(f'{'-'*50}IsLtP{'-'*50}')
print(IsLtP(MakePecahan(1,2), MakePecahan(1,2)))
print(IsLtP(MakePecahan(1,2), MakePecahan(3,3)))
print(IsLtP(MakePecahan(3,3), MakePecahan(1,2)))