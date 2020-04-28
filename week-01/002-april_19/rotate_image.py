# ------------------------------------
#                DAY 2
#       Amazon, Microsoft & Apple 
#          Interview Question
#
#            ROTATE IMAGE
#  You are given an nxn 2D matrix that
#  represents an image. Rotate the ima-
#  ge by 90 degrees (clockwise)
#
# by: @estalvgs1999
# -------------------------------------

test_image = [[1,2,3],
              [4,5,6],
              [7,8,9]]

# SOLUTION 1
# This simple algorithm allows you to rotate an 
# image without the need to use extra space, in 
# just two steps.

def rotate_img(image):
    
    # Step 1. Transpose Matrix 
    image = transpose(image)

    # Step 2. Flip Horizontally
    image = flip_rows(image)
    
    return image

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

# Function to show matrix 
def show_image(image):
    print('-'*10)
    for row in image:
        print(row)

if __name__ == "__main__":

    show_image(test_image)
    rt_image = rotate_img(test_image)
    show_image(rt_image)