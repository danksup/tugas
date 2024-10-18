#3+6+9+12+15+.......

def s(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    else:
        return n * 3 + s(n-1) 

print(s(1)) # 3 = 3
print(s(2)) # 3 + 6 = 9
print(s(3)) # 3 + 6 + 9 = 18
print(s(4)) # 3 + 6 + 9 + 12 = 30
print(s(5))