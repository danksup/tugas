# Nama File   = tugasgaris.py
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 8 Oktober 2024
# Deskripsi   = Didefinisikan suatu type bernama Garis, yang mewakili suatu garis. terdiri dari 2 point.

# DEFINISI TYPE GARIS
# type point : <point1: point, point2: point>
#   {<point1, point2> adalah sebuah point, dengan x adalah absis, y adalah ordinat}

# DEFINISI TYPE POINT
# type point : <x: real, y: real>
#   {<x, y> adalah sebuah point, dengan x adalah absis, y adalah ordinat}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis : point -> real
#   {Absis(P) Memberikan Absis Point P}
# Ordinat : point -> real
#   {Ordinat(P) Memberikan ordinat Point P}
# GetT1 : garis -> point
#   {Gett1(g) mengembalikan point pertama sebuah garis}
# GetT2 : garis -> point
#   {Gett2(g) mengembalikan point kedua sebuah garis}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeLine: 2 point -> garis
#   {MakeLine(p1, p2) menghasilkan garis terhadap 2 point}

# DEFINISI OPERATOR/FUNGSI LAIN TERHADAP GARIS
# PanjangGaris: garis -> real
#   {PanjangGaris(g) menghitung jarak garis dan menghasilkan nilai real}
# gradien : garis -> real
#   {gradien(g) menghitung gradien sebuah garis dan menghasilkan nilai real}

# DEFINISI DAN SPESIFIKASI PREDIKAT TERHADAP GARIS
# is_sejajar: 2 garis -> boolean
#   {is_sejajar(g1,g2) menghasilkan nilai boolean True jika 2 garis saling sejajar}
# istegakLurus: 2 garis -> boolean
#   {is_sejajar(g1,g2) menghasilkan nilai boolean True jika 2 garis saling tegak lurus}

#REALISASI
def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

def getT1(g):
    return g[0]

def getT2(g):
    return g[1]

def fx2(x):
    return x*x

def PanjangGaris(g):
    return (fx2((absis(getT2(g)) - absis(getT1(g)))) + fx2(ordinat(getT2(g)) - ordinat(getT1(g)))) ** 0.5

def gradien(g):
    return (ordinat(getT2(g)) - ordinat(getT1(g))) / (absis(getT2(g)) - absis(getT1(g)))

def is_sejajar(g1, g2):
    return gradien(g1) == gradien(g2)

def isTegakLurus(g1, g2):
    return gradien(g1) * gradien(g2) == -1


print(is_sejajar(((1,2),(4,5)),((6,7),(8,9))))
print(is_sejajar(((1,2),(4,5)),((2,7),(8,9))))
print(isTegakLurus(((1,2),(4,5)),((2,7),(8,9))))
print(isTegakLurus(((4,0),(6,-5)),((4,2),(0,6))))
print(PanjangGaris(((1,2), (3,4))))
