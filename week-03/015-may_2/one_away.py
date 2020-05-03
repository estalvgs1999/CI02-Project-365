# ---------------------------------------
#                  DAY 15
#         Coding Interview Question
#
#                 ONE AWAY
# There are three types of edits that can
# be performed on strings: 
# 
#   insert a character -> len(str1) < len(str2)
#   remove a character -> len(str1) > len(str2)
#   replace a character -> len(str1) = len(str2)
# 
# Given two strings, write a function to 
# check if they are one edit (or zero 
# edits) away.
#  
# EXAMPLE
#   pale,ple -> true
#   pales, pale -> true
#   pale, bale -> true
#   pale, bae -> false
# 
# Question 1.5 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

def one_away(s1,s2):
    n,m = len(s1),len(s2)
    if n < m:
        return check_insert(s1,s2) # Insert Case
    elif n > m:
        return check_insert(s2,s1) # Remove Case
    else:
        return check_replace(s1,s2) # Replace Case

def check_replace(s1,s2):
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference: 
                return False
            found_difference = True
    return True

def check_insert(s1,s2):
    a,b = 0,0

    while a < len(s1) and b < len(s2):
        if s1[a] != s2[b]:
            if a != b: 
                return False
            b += 1
        else:
            a += 1; b += 1
    return True