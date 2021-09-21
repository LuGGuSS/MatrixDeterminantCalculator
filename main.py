# Getting matrix size
import copy

N = int(input("Input matrix size: "))

Matrix = []

for i in range(0, N):
    line = []
    for j in range(0, N):
        line.append(int(input("Input number on position " + str(i + 1) + " " + str(j + 1) + ": ")))
    Matrix.append(line)

# Printing matrix out
for i in range(0, N):
    for j in range(0, N):
        print(str(Matrix[i][j]) + " ", end="")
    print("")


def calc(n, matrix):  # Function that calculates determinant
    if n == 2:  # If matrix is a size of 2 - calculates det and returns it
        d = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return d
    else:
        d = int(0)
        temp = copy.deepcopy(matrix)
        line = copy.deepcopy(temp[0])  # Copying a line of numbers and then deleting it
        temp.pop(0)
        for j in range(0, n):
            temp2 = copy.deepcopy(temp)
            for k in range(0, n-1):  # Deleting all number in a specified column
                temp2[k].pop(j)
            d += ((-1) ** (0 + j + 2)) * line[j] * (calc(n - 1, temp2))
        return d


print("")
print(str(calc(N, Matrix)))
