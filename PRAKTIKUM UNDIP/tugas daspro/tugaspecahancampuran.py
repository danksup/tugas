# Nama File   = tugaspecahancampuran.py
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 8 Oktober 2024
# Deskripsi   = Didefinisikan suatu type bernama pecahan campuran, yang terdiri dari bilangan bulat, pembilang, dan penyebut.

#DEFINISI DAN SPESIFIKASI TYPE PECAHAN CAMPURAN
# type pecahanc: <bil: integer, n: integer ≥ 0, d: integer > 0>
#   {mendefinisikan pecahan campuran dengan bil adalah bilangan bulat n adalah pembilang (numerator) dan d adalah penyebut (denumerator). Penyebut sebuah Pecahan tidak boleh 0}

#DEFINISI DAN SPESIFIKASI TYPE PECAHAN
# type pecahan: <n: integer >=0;d integer >0>
#  {hanya mendefinisikan pecahan biasa yang terdiri dari  numerator dan denumerator}

#DEFINISI DAN SPESIFIKASI SELEKTOR 
# bilbul : pecahanc -> integer 
#   {bilbul(x) memberikan bilangan bulat dari pecahan tersebut}
# pembilang : pecahanc -> integer >=0
#   {pembilang(x) memberikan numerator pembilang n dari pecahan tersebut}
# penyebut : pecahanc -> integer >0
#   {penyebut(x) memberikan denumerator penuyebut d dari pecahan tersebut}

#DEFINISI DAN SPESIFIKASI KONTRUKTOR
# MakePecahanC : <integer ,integer >=0, integer> > 0 -> pecahanc
#   {MakePecahanC(bil, x,y) membentuk seuah pecahan campuran dari bilangan bulat bil pembilang x dan penyebut y, dengan bil, x, dan y integer}

#DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN CAMPURAN
#   { Operator aritmatika Pecahan }
# KonversiPecahan : pecahanc -> pecahan
#   { KonversiPecahan(P) mengubah pecahan campuran P menjadi pecahan biasa}
# AddP : 2 pecahanc → pecahanc
#   { AddP(P1, P2) : Menambahkan dua buah pecahan campuran P1 dan P2}
# SubP : 2 pecahanc → pecahanc
#   { SubP(P1, P2) : Mengurangkan dua buah pecahan campuran P1 dan P2 Mengurangkan dua pecahan  }
# MulP : 2 pecahanc → pecahanc
#   { MulP(P1, P2) : Mengalikan dua buah pecahan campuran P1 dan P2 Mengalikan dua pecahan }
# DivP : 2 pecahanc → pecahanc
#   { DivP(P1, P2) : Membagi dua buah pecahan campuran P1 dan P2 Membagi dua pecahan }
# KonversiReal : pecahanc → real
#   { KonversiReal(P) Menuliskan bilangan pecahan campuran dalam notasi desimal }

#DEFINISI DAN SPESIFIKASI PREDIKAT
# { Operator relasional Pecahan }
# IsEqP? : 2 pecahanc → boolean
#    { IsEqP?(p1, p2) true jika p1 = p2 Membandingkan apakah dua buah pecahan sama nilainya }
# IsLtP? : 2 pecahanc → boolean
#   { IsLtP?(p1, p2) true jika p1 < p2 Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2}
# IsGtP? : 2 pecahanc → boolean
#   { IsGtP?(p1, p2) true jika p1 > p2 Membandingkan nilai dua buah pecahan, apakah p1 lebih besar nilainya dari p2 }

#REALISASI
def bilbul(bil):
    return int(bil[0])

def pembilang(n):
    return int(n[1])

def penyebut(d):
    return int(d[2])

def MakePecahanc(bil, n, d):
    return f'{bil} {n}/{d}'

def KonversiPecahan(p):
    if penyebut(p) < 0 and pembilang(p) < 0:
        return f'{(penyebut(p) * -1) * bilbul(p) + (pembilang(p) * -1)}/{penyebut(p) * -1}'
    elif bilbul(p) < 0 and pembilang(p) < 0:
        return f'{penyebut(p) * (bilbul(p) * -1) + (pembilang(p) * -1)}/{penyebut(p)}'
    elif bilbul(p) < 0 and penyebut(p) < 0:
        return f'{(penyebut(p) * -1) * bilbul(p) + pembilang(p)}/{penyebut(p) * -1}'
    else:
        return f'{penyebut(p) * bilbul(p) + pembilang(p)}/{penyebut(p)}'

def AddP(p1, p2):
    return MakePecahanc(
        bilbul(p1) + bilbul(p2),
        pembilang(p1) * penyebut(p2) + pembilang(p2) * penyebut(p1),
        penyebut(p1) * penyebut(p2)
    )

def SubP(p1, p2):
    return MakePecahanc(
        bilbul(p1) - bilbul(p2),
        pembilang(p1) * penyebut(p2) - pembilang(p2) * penyebut(p1),
        penyebut(p1) * penyebut(p2)
    )

def MulP(p1, p2):
    return MakePecahanc(
        ((pembilang(p1) + bilbul(p1) * penyebut(p1)) * (pembilang(p2) + bilbul(p2) * penyebut(p2))) // (penyebut(p1) * penyebut(p2)),
        ((pembilang(p1) + bilbul(p1) * penyebut(p1)) * (pembilang(p2) + bilbul(p2) * penyebut(p2))) % (penyebut(p1) * penyebut(p2)),
        penyebut(p1) * penyebut(p2)
    )

def DivP(p1, p2):
    return MakePecahanc(
        ((pembilang(p1) + bilbul(p1) * penyebut(p1)) * penyebut(p2)) // (penyebut(p1) * (pembilang(p2) + bilbul(p2) * penyebut(p2))),
        ((pembilang(p1) + bilbul(p1) * penyebut(p1)) * penyebut(p2)) % (penyebut(p1) * (pembilang(p2) + bilbul(p2) * penyebut(p2))),
        penyebut(p1) * (pembilang(p2) + bilbul(p2) * penyebut(p2))
    )

def KonversiReal(x):
    return bilbul(x) + pembilang(x) / penyebut(x)

def IsEqP(p1, p2):
    return (pembilang(p1) + bilbul(p1) * penyebut(p1)) * penyebut(p2) == (pembilang(p2) + bilbul(p2) * penyebut(p2)) * penyebut(p1)

def IsLtP(p1, p2):
    return (pembilang(p1) + bilbul(p1) * penyebut(p1)) * penyebut(p2) < (pembilang(p2) + bilbul(p2) * penyebut(p2)) * penyebut(p1)

def IsGtP(p1, p2):
    return (pembilang(p1) + bilbul(p1) * penyebut(p1)) * penyebut(p2) > (pembilang(p2) + bilbul(p2) * penyebut(p2)) * penyebut(p1)


#APLIKASI
print(f'{'-'*50}konversi pecahan{'-'*50}')
print(KonversiPecahan((-12,1,3)))

print(f'{'-'*50}konversi real{'-'*50}')
print(KonversiReal((-12,1,3)))

print(f'{'-'*50}AddP{'-'*50}')
print(AddP((12,1,3),(9,1,5)))

print(f'{'-'*50}SubP{'-'*50}')
print(SubP((12,1,3),(9,1,5)))

print(f'{'-'*50}MulP{'-'*50}')
print((MulP((12,1,3),(9,1,5))))

print(f'{'-'*50}DivP{'-'*50}')
print(DivP((12,1,3),(9,1,5)))

print(f'{'-'*50}IsEqP{'-'*50}')
print(IsEqP((12,1,3),(9,1,5)))

print(f'{'-'*50}IsGtP{'-'*50}')
print(IsGtP((12,1,3),(9,1,5)))

print(f'{'-'*50}IsLtP{'-'*50}')
print(IsLtP((12,1,3),(9,1,5)))



