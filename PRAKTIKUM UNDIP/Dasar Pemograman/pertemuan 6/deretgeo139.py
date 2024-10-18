def f(n):
    if n == 1:
        return 3
    else:
        return 3*f(n-1)
    
print(f(1))
print(f(3))
print(f(9))