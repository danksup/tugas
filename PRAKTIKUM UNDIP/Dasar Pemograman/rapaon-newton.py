import os
import time
start_time = time.time()

def polynomial(a):
    penyimpanan = []
    selector = a.replace(" ", "").replace("-", "+-").split("+")
    
    for var in selector:
        if 'x' in var:
            if '^' in var:
                koef, power = var.split('x^')
                power = int(power)  
            else:
                koef = var.split('x')[0]
                power = 1
        else:
            koef = var
            power = 0
        
        if koef == '' or koef == '+': 
            koef = 1  
        elif koef == '-':
            koef = -1 
        else:
            koef = int(koef) 

        penyimpanan.append((koef, power))
    
    penyimpanan.sort(key=lambda x: x[1], reverse=True)
    
    return penyimpanan

def hitung(koefisien, x):
    result = 0
    for koef, pangkat in koefisien:
        result += koef * (x ** pangkat)
    return result

def uh(a):
    angka = polynomial(a)
    
    konstanta = [coef for coef, pangkat in angka if pangkat == 0]
    
    if not konstanta:
        kfc = 0
    else:
        kfc = konstanta[0]
    
    kfc_factor = []
    for i in range(1, abs(kfc) + 1):
        if kfc % i == 0:
            kfc_factor.extend([i, -i])  
    
    hasil = {}
    for factor in kfc_factor:
        hasil[factor] = hitung(angka, factor)
    
    print(hasil)
    return hasil

def pencari_faktor(a):
    hei = uh(a)
    factor = []
    for k, v in hei.items():
        if v == 0:
            factor.append(k)
    
    if not factor:
        return f'{a} tidak punya persamaan rasional'
    else:
        return factor

os.system('clear')
print(pencari_faktor('5x^2 + 2x + 6'))
print(f'{"-" * 50} divisor {"-"*50}')
print(pencari_faktor('x^2 - 1'))
print(f'{"-" * 50} divisor {"-"*50}')
print(pencari_faktor('4x^2 + 5x + 6'))
print(f'{"-" * 50} divisor {"-"*50}')
print(pencari_faktor('x^2 - 5x - 6'))
print(f'{"-" * 50} divisor {"-"*50}')
print(pencari_faktor('x^3 - 6x^2 + 11x - 6'))



print("--- %s seconds ---" % (time.time() - start_time))