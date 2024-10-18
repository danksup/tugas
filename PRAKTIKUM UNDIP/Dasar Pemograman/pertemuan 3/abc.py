def quad(a,b,c):
    D = diskrim(b,a,c)
    if D < 0:
        return "tidak ada penyelesaian"
    
    neg_side = (-b - (D ** (1/2))) / (2 * a)
    pos_side = (-b + (D ** (1/2))) / (2 * a)
    if pos_side > neg_side:
        return neg_side,pos_side
    elif neg_side > pos_side:
        return pos_side, neg_side 
    else:
        return pos_side, neg_side

def diskrim(b,a,c):
    return (b ** 2) - (4 * a * c)

print(quad(1,-6,85))
print(quad(1,-6,5))
print(quad(1,3,1))
print(quad(1,8,12))
