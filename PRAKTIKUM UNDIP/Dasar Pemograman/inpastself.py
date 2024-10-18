def se(x,y):
    if x == 0:
        return 0
    else:
        return se(x-1, 101111) + y
    
print(se(9,20))