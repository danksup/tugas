def wujud_air(x):
    if x > 100:
        return f'wujud air pada suhu {x} adalah es'
    elif x > 0 and x < 100:
        return f'wujud air pada suhu {x} adalah cair'
    elif x < 100:
        return f'wujud air pada suhu {x} adalah uap'
    
print(wujud_air(12))
print(wujud_air(2))
print(wujud_air(-12))
print(wujud_air(102))
print(wujud_air(0.9))