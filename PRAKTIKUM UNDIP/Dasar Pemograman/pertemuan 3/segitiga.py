def segitiga(a,b,c):
    if a == 0 or b == 0 or c == 0:
        return "angka tidak boleh kurang dari 1"
    else:
        if a == b and a == c and b == c:
            return ("segitiga sama sisi")
        elif a == b or b == c or a == c:
            return "segitiga sama kaki"
        elif a != b and b != c or b != c:
            return "segitiga sebarang"
        

segitiga1 = segitiga(3,2,5)

print(segitiga1)