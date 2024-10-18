# Nama File   = konversi_temp.oy
# Nama        = Agung Rama Pramana Putra
# Tanggal     = 9 September 2024
# Deskripsi   = gak tau 

# DEFINISI DAN SPESIFIKASI 
# max(d,m,y): real--> 3 real
#   {menentukan nilai maximal dari 2 bilangan }

def konversi_celcius(int_value):
    c_to_f = (int_value * 9/5) + 32
    c_to_k = int_value + 273.15
    c_to_r = (int_value * 4/5)

    return f'{c_to_f}F, {c_to_k}K, {c_to_r}R'

duabelasderajatcelcius = konversi_celcius(12)
print(duabelasderajatcelcius)
