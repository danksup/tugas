a = [6 ,7, 8]
b = [1, 7, 8]

def compareTriplets(a, b):
    if a[0] > b[0] or a[1] > b[1] or a[2] > b[2]:
        return 1
    elif a[0] < b[0] or a[1] < b[1] or a[2] < b[2]:
        return 1
    elif a[0] == b[0] or a[1] == b[1] or a[2] == b[2]:
        return None
    
a = [6 ,7, 8]
b = [0, 7, 9]

print(compareTriplets(a,b))