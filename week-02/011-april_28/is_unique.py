# ---------------------------------------
#                   DAY 11
#         Coding Interview Question
#
#                 IS UNIQUE
#  Implement an algorithm to determine if
#  a string has all unique characters.
#  What if you cannot use additional data
#  structures?
#
#  (!) Asumming that is an ASCII string
#
#  Question 1.1 | ctci 6th edition
#
#  by: @estalvgs1999
# ----------------------------------------


# Best Solution
# Time Complexity => O(n), n is the length of the string
# Space Complexity => O(1)

def is_unique(string):

    # We immediately return false if the string length 
    # is bigger than 128 (ASCII has a 128-character alphabet)
    if len(string) > 128: return False

    char_set = [False for _ in range(128)]

    for char in string:
        val = ord(char)
        if char_set[val]: return False
        char_set[val] = True

    return True


# Not using Data Structures
# Time Complexity => O(n²), n is the length of the string
# Space Complexity => O(1)
# These solution are not as optimal in some respects, but might 
# be better depending on the constraints of the problem
    
def is_unique_nDS(string):
    
    n = len(string)

    for i in range(n-1):
        for j in range(i+1,n):
            if string[i] == string[j]:
                return False
    return True

