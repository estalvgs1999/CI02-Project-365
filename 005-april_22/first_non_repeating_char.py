# ---------------------------------------
#                  DAY 5
#        Google Interview Question
#
#      FIRST NON REPEATING CHARACTER
#  Given a character string returns the 
#  first character that is not repeated.
#  If dont exists return _ (underscore)
#  
#  Input string contains only lowercase 
#  english letters.
#  Input String Length 1 < n < 100 000
#
#  by: @estalvgs1999
# ---------------------------------------

# Complexity => O(n²)
def bf_first_non_repeating_character(s): # brute force solution

    n = len(s)
    for i in range(n):
        seen_duplicated = False
        for j in range(n):
            if s[i] == s[j] and i != j:
                seen_duplicated = True
                break
        if not seen_duplicated: return s[i]
    return '_'

# Complexity => O(n²)
def hm_first_non_repeating_character(s):
    char_counts = {}

    for c in s:
        if c in char_counts.keys():
            char_counts[c]+=1
        else:
            char_counts[c]=1

    for c in char_counts:
        if char_counts[c] == 1: return c

    return '_'

# Complexity => O(n)
def first_non_repeating_character(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_' 


if __name__ == "__main__":
    import tests
    tests.run_test()
     