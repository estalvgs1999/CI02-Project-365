# ---------------------------------------
#                  DAY 17
#         Coding Interview Question
#
#              ROTATE MATRIX
#  Given an image represented by an NxN 
#  matrix, where each pixel in the image
#  is 4 bytes, write a method to rotate
#  the image by 90 degrees. 
#  Can you do this in place?
#  
#  Question 1.7 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

# Complexity => O(n²) 
# which is the best we can do since any algorithm
# must touch all n² elements.

def rotate_matrix(matrix):
    
    # Step 1. Transpose Matrix 
    matrix = transpose(matrix)

    # Step 2. Flip Horizontally
    matrix = flip_rows(matrix)
    
    return matrix

# Turns rows to columns
def transpose(matrix):
    n = len(matrix[0])
    for i in range(n):
        for j in range(i,n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    return matrix

# Invert the order of the rows of an array
def flip_rows(matrix):
    n = len(matrix[0])
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix