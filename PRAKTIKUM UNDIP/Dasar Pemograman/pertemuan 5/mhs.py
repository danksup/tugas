# Nama File   = mhs.py
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 29 September 2024
# Deskripsi   = tipe bentukan yang merepresentasikan data mahasiswa, nilai, dan mata kuliah.

# DEFINISI DAN SPESIFIKASI SELEKTOR
# nim: mahasiswa -> string
#   {nim(x) memberikan NIM (Nomor Induk Mahasiswa) dari mahasiswa x}
# nama: mahasiswa -> string
#   {nama(x) memberikan nama mahasiswa dari mahasiswa x}
# tgl_lahir: mahasiswa -> tuple
#   {tgl_lahir(x) memberikan tanggal lahir mahasiswa dari mahasiswa x}
# kode_matkul: mahasiswa -> string
#   {kode_matkul(x) memberikan kode mata kuliah dari mahasiswa x}
# nama_matkul: mahasiswa -> string
#   {nama_matkul(x) memberikan nama mata kuliah dari mahasiswa x}
# nilai: mahasiswa -> int
#   {nilai(x) memberikan nilai mata kuliah dari mahasiswa x}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# mahasiswa: string, string, tuple, string, string, int -> mahasiswa
#   {mahasiswa(nim_m, nama_m, tgl_lahir_m, kode_matkul_m, nama_matkul_m, nilai_m) membentuk
#    tipe bentukan mahasiswa dari NIM, nama, tanggal lahir, kode mata kuliah, nama mata kuliah, dan nilai}
# MHS1: mahasiswa -> tuple
#   {MHS1(x) memberikan tuple yang berisi NIM, nama, dan tanggal lahir mahasiswa x}
# MHS2: mahasiswa -> tuple
#   {MHS2(x) memberikan tuple yang berisi NIM, kode mata kuliah, dan nilai mahasiswa x}
# MHS3: mahasiswa -> tuple
#   {MHS3(x) memberikan tuple yang berisi kode mata kuliah dan nama mata kuliah mahasiswa x}

# DEFINISI DAN SPESIFIKASI PREDIKAT
# hitung_range_nilai: tuple, tuple -> string
#   {hitung_range_nilai(data1, data2) memberikan string yang berisi informasi 
#    mengenai nilai tertinggi, nilai terendah, dan range nilai jika kedua mahasiswa memiliki mata kuliah yang sama.
#    Jika mata kuliahnya berbeda, akan mengembalikan pesan 'Matkul berbeda'.}


# REALISASI
def nim(x):
    return x[0]

def nama(x):
    return x[1]

def tgl_lahir(x):
    return x[2]

def kode_matkul(x):
    return x[3]

def nama_matkul(x):
    return x[4]

def nilai(x):
    return x[5]

def MHS1(x):
    return nim(x), nama(x), tgl_lahir(x)

def MHS2(x):
    return nim(x), kode_matkul(x), nilai(x)

def MHS3(x):
    return kode_matkul(x), nama_matkul(x)

def mahasiswa(nim_m, nama_m, tgl_lahir_m, kode_matkul_m, nama_matkul_m, nilai_m):
    return [nim_m, nama_m, tgl_lahir_m, kode_matkul_m, nama_matkul_m, int(nilai_m)]  

def hitung_range_nilai(data1, data2):
    if data1[1] != data2[1]:
        return 'Matkul berbeda'
    else:
        return f'NIM: {data1[1]},Nilai Tertinggi: {max(data1[2], data2[2])}, Nilai Terendah: {min(data1[2], data2[2])}, Range Nilai: {abs(data1[2] - data2[2])}'

print(hitung_range_nilai(MHS2(mahasiswa('1000', "Nama Siswa Pratama", (12,1,2005), 'K001', "Struktur Dasar", '95')),
                        MHS2(mahasiswa('1001', "Nama Siswa Dwitama", (9,1,2005), 'K001', "Dasar Struktur", '77'))))
 
print(hitung_range_nilai(MHS2(mahasiswa('1000', "Nama Siswa Pratama", (12,1,2005), 'K005', "Sistem Pemograman", '90')),
                        MHS2(mahasiswa('1001', "Nama Siswa Dwitama", (9,1,2005), 'K005', "Sistem Pemograman", '100'))))

print(hitung_range_nilai(MHS2(mahasiswa('1000', "Nama Siswa Pratama", (12,1,2005), 'K001', "Struktur Dasar", '95')),
                        MHS2(mahasiswa('1001', "Nama Siswa Dwitama", (9,1,2005), 'K005', "Sistem Pemograman", '100'))))
