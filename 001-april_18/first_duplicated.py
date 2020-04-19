# ------------------------------------
#                DAY 1
#      Google Interview Question
#
#          FIRST DUPLICATED
#  Find the first duplicate element in 
#  a given an integer array. 
#  Find the most efficient solution 
#  possible.
#  
#  The restrictions are: the value of 
#  the elements of the array go from 
#  1 to N, where N is the length of 
#  the array. 
#  Obviously the elements can be 
#  duplicated. 
#  If there are no duplicate elements 
#  it returns -1.
#
# by: @estalvgs1999
# -------------------------------------

# SOLUTION 1

test_array = [2,1,4,5,3,6]

def first_duplicated(a):
    top = len(a)
    min_match_index = top

    for i in range(top):
        for j in range(i+1,top):
            if a[i] == a[j]:
                min_match_index = min(min_match_index,j)
    
    if min_match_index == top: return -1
    return a[min_match_index] 



if __name__ == "__main__":
    print(first_duplicated(test_array))