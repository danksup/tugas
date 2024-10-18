def temp(int_value):
    c_to_f = (int_value * 9/5) + 32
    c_to_k = int_value + 273.15
    c_to_r = (int_value * 4/5)

    return(c_to_f, c_to_k, c_to_r)


erm = temp(2)
print(erm)

