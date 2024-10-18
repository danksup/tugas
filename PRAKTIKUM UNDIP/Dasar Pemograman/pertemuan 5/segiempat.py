# Nama File   = segiempat.py
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 29 September 2024
# Deskripsi   = tipe bentukan yang merepresentasikan segiempat.

# DEFINISI DAN SPESIFIKASI SELEKTOR
# sisi1: sisi -> int
#   {sisi1(a) memberikan sisi ke-satu dari segiempat}
# sisi2: sisi -> int
#   {sisi2(a) memberikan sisi ke-dua dari segiempat}
# sisi3: sisi -> int
#   {sisi3(a) memberikan sisi ke-tiga dari segiempat}
# sisi4: sisi -> int
#   {sisi4(a) memberikan sisi ke-empat dari segiempat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeRect: 4 int -> segiempat
#   {MakeRect(a,b,c,d) membentuk sebuah segiempat dari 4 integer a,b,c,d}

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isbujursangkar: segiempat -> boolean
#   {isbujursangkar(s) mengembalikan nilai boolean. jika semua sisi-sisi sama akan mengembalikan true, sebaliknya false}

# DEFINISI OPERATOR/FUNGSI LAIN TERHADAP POINT
# isjajargenjang: segiempat -> boolean
#   {isbujursangkar(s) mengembalikan nilai boolean. jika semua 2 sisi sejajar bernilai sama akan mengembalikan true, sebaliknya false}
# areabujursangakar: segiempat -> int
#   {areabujursangkar(s) mengembalikan nilai perkalian dari salah 2 sisi bujursangkar}

# REALISASI
def sisi1(a):
    return a[0]

def sisi2(a):
    return a[1]

def sisi3(a):
    return a[2]

def sisi4(a):
    return a[3]

def MakeRect(a,b,c,d):
    return [a,b,c,d]

def isbujursangkar(s):
    return s[0] == s[1] == s[2] == s[3]

def isjajargenjang(s):
    return (s[0] == s[2]) and (s[1] == s[3])

def areabujursangkar(s):
    if isbujursangkar(s):
        return s[0] * s[1] or s[2] * s[3]
    return 'bukan bujur sangkar'

print(isbujursangkar(MakeRect(4,4,4,4))) 
print(isjajargenjang(MakeRect(4,4,4,4)))  
print(areabujursangkar(MakeRect(4,4,4,4)))   
print(areabujursangkar(MakeRect(1,4,4,4)))                             