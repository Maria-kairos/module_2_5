matrix = []
def get_matrix(n,m,value):
    matrix1 = []
    for i in range(n):
        matrix1 = []
        for h in range(m):
            matrix1.append(value)
        matrix.append(matrix1)

get_matrix(5,3,34)
print(matrix)
