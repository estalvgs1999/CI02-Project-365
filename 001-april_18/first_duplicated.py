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


test_array = [2,1,3,5,3,2]

# SOLUTION 1
# complexity => O(n²)
# What if it were a billion-item array? 
# This algorithm uses a nested double loop, 
# and this is not efficient at all.

def first_duplicated_1(a):
    top = len(a)
    min_match_index = top

    for i in range(top):
        for j in range(i+1,top):
            if a[i] == a[j]:
                min_match_index = min(min_match_index,j)
    
    if min_match_index == top: return -1
    return a[min_match_index] 

# SOLUTION 2
# complexity => O(n)
# This algorithm provides a better solution, 
# its linear, it does not check the entire array, 
# except in the worst case where the repeated 
# element is the last one and the whole array 
# must be checked.
# The problem with this solution is that it uses 
# a lot of memory. (in larger cases)

def first_duplicated_2(a):
    visited_elements = set([])

    for x in a:
        if x in visited_elements: # x in set => O(n)
            return x
        visited_elements.add(x)
    return -1

# SOLUTION 3
# complexity => O(n)
# A brilliant idea!
# Its not very intuitive but highly efficient, 
# we still have linear complexity but without 
# using extra memory!

def first_duplicated_3(a):
        
    for x in a:
        x = abs(x)
        if a[x-1] < 0:
            return x
        a[x-1] = -a[x-1]
    return -1


if __name__ == "__main__":
    print("TEST 1: ",first_duplicated_1(test_array))
    print("TEST 2: ",first_duplicated_2(test_array))
    print("TEST 3: ",first_duplicated_3(test_array))