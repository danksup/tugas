rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at row {i+1}, column {j+1}: "))
        row.append(element)
    matrix.append(row)

print("The matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))
