# ---------------------------------------
#                  DAY 18
#         Coding Interview Question
#
#               ZERO MATRIX
#  Write an algorithm such that if an
#  element in an MxN matrix is 0, its
#  entire row and column are set to 0.
#  
#  Question 1.8 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

# Complexity => O(n²)
def zero_matrix(matrix):

    zero_row = []
    zero_col = []

    for i in range(len(matrix)):

        if 0 in matrix[i]:
            zero_row.append(i)

            # We look for the columns in which there are zeros
            for j in range(len(matrix[i])):
               if matrix[i][j] == 0:
                    if not j in zero_col:
                        zero_col.append(j)

    # Nullify all rows in zero_row
    for row in zero_row:
        matrix[row] = [0 for _ in range(len(matrix))]

    # Nullify all columns in zero_col 
    for i in range(len(matrix)):
        for col in zero_col:
            matrix[i][col] = 0

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    matrix = [ [0,1,1],
               [1,1,0],
               [1,1,1]]
    print_matrix(zero_matrix(matrix))