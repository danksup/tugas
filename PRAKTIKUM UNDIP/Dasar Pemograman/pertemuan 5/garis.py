# Nama File   = garis.py
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 29 September 2024
# Deskripsi   = Didefinisikan suatu type bernama Point, yang mewakili suatu titik dalam koordinat kartesian, terdiri dari absis dan ordinat.

# DEFINISI TYPE
# type point : <x: real, y: real>
#   {<x, y> adalah sebuah point, dengan x adalah absis, y adalah ordinat}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis : point -> real
#   {Absis(P) Memberikan Absis Point P}

# Ordinat : point -> real
#   {Ordinat(P) Memberikan ordinat Point P}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint : 2 real -> point
#   {MakePoint(a,b) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat}

# DEFINISI DAN SPESIFIKASI PREDIKAT
# is_sejajar: 2 garis -> boolean
#   {is_sejajar(g1,g2) menghasilkan nilai boolean jika 2 garis saling sejajar}

# DEFINISI OPERATOR/FUNGSI LAIN TERHADAP POINT
# panjang_garis: 1 garis -> real
#   {panang_garis(p1,p2) menghitung jarak garis dan menghasilkan nilai real}

#REALISASI
def MakeLine(x1,y1,x2,y2):
    return ((x1,y1),(x2,y2))

def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

# def panjang_gari1(p1, p2):
#     return (((absis(p2) - absis(p1))**2 + (ordinat(p2) - ordinat(p1))**2)**0.5)

def panjang_garis(g):
    return ((absis(g[1]) - absis(g[0])) **2 + (ordinat(g[1]) - ordinat(g[0]))**2)**0.5

def is_sejajar(g1, g2):
    return (ordinat(g1[1]) - ordinat(g1[0])) / (absis(g1[1]) - absis(g1[0])) == (ordinat(g2[1]) - ordinat(g2[0])) / (absis(g2[1]) - absis(g2[0]))


print(is_sejajar(((1,2),(4,5)),((6,7),(8,9))))
print(is_sejajar(((1,2),(4,5)),((2,7),(8,9))))
print(panjang_garis(((1,2), (3,4))))
# print(panjang_gari1((1,2), (3,4)))