def temp_convert():
    temp_list = ['c', 'f', 'r', 'k', 'celcius', 'fahrenheit', 'reamur', 'kelvin']

    def check_unit(unit):
        return unit.lower() in temp_list

    print("Unit: Celcius, Fahrenheit, Kelvin, Reamur")

    converted_unit = input("unit apa yang ingin dikonversi: ").lower()
    if not check_unit(converted_unit):
        return print("Unit tidak valid")

    to_unit = input("dikonversi ke: ").lower()
    if not check_unit(to_unit):
        return print("Unit tidak valid")

    temp_value = input("masukkan value: ")
    int_value = int(temp_value)

    if converted_unit == 'c' or converted_unit == 'celcius':
        c_to_f = (int_value * 9/5) + 32
        c_to_k = int_value + 273.15
        c_to_r = (int_value * 4/5)

        if to_unit == 'f' or to_unit == 'fahrenheit':
            return print(f'{int_value}C ke Fahrenheit adalah {c_to_f}F')
        elif to_unit == 'k' or to_unit == 'kelvin':
            return print(f'{int_value}C ke Kelvin adalah {c_to_k}K')
        elif to_unit == 'r' or to_unit == 'reamur':
            return print(f'{int_value}C ke Reamur adalah {c_to_r}R')
        elif to_unit == 'all':
            return print(f'{int_value}C ke Fahrenheit adalah {c_to_f}F\n{int_value}C ke Kelvin adalah {c_to_k}K\n{int_value}C ke Reamur adalah {c_to_r}R ')
        
    elif converted_unit == 'f' or converted_unit == 'fahrenheit':
        f_to_c = (int_value - 32) * 5/9
        f_to_k = (int_value + 459.67) * 5/9
        f_to_r = 4/9 * (int_value - 32)

        if to_unit == 'c' or to_unit == 'celcius':
            return print(f'{int_value}F ke Celcius adalah {f_to_c}F')
        elif to_unit == 'k' or to_unit == 'kelvin':
            return print(f'{int_value}F ke Kelvin adalah {f_to_k}K')
        elif to_unit == 'r' or to_unit == 'reamur':
            return print(f'{int_value}F ke Reamur adalah {f_to_r}R')
        elif to_unit == 'all':
            return print(f'{int_value}F ke Celcius adalah {f_to_c}F\n{int_value}F ke Kelvin adalah {f_to_k}K\n{int_value}F ke Reamur adalah {f_to_r}R ')
        
    elif converted_unit == 'k' or converted_unit == 'kelvin':
        k_to_f = (int_value * 9/5) - 459.67
        k_to_c = int_value - 273.15
        k_to_r = (int_value * 4/5)

        if to_unit == 'f' or to_unit == 'fahrenheit':
            return print(f'{int_value}K ke Fahrenheit adalah {k_to_f}F')
        elif to_unit == 'c' or to_unit == 'celcius':
            return print(f'{int_value}K ke Celcius adalah {k_to_c}C')
        elif to_unit == 'r' or to_unit == 'reamur':
            return print(f'{int_value}K ke Reamur adalah {k_to_r}R')
        elif to_unit == 'all':
            return print(f'{int_value}K ke Fahrenheit adalah {k_to_f}F\n{int_value}K ke Celcius adalah {k_to_c}C\n{int_value}K ke Reamur adalah {k_to_r}R ')
        
    elif converted_unit == 'r' or converted_unit == 'reamur':
        r_to_f = (int_value * 2.25) + 32
        r_to_k = (int_value / 0.8) + 273.15
        r_to_c = (int_value * 0.8)

        if to_unit == 'f' or to_unit == 'fahrenheit':
            return print(f'{int_value}R ke Fahrenheit adalah {r_to_f}F')
        elif to_unit == 'k' or to_unit == 'kelvin':
            return print(f'{int_value}R ke Kelvin adalah {r_to_k}K')
        elif to_unit == 'c' or to_unit == 'celcius':
            return print(f'{int_value}R ke Celcius adalah {r_to_c}R')
        elif to_unit == 'all':
            return print(f'{int_value}R ke Fahrenheit adalah {r_to_f}F\n{int_value}R ke Kelvin adalah {r_to_k}K\n{int_value}R ke Celcius adalah {r_to_c}R ')
    else:
        return print("tidak tersedia")


temp_convert()