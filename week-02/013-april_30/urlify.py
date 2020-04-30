# ---------------------------------------
#                   DAY 13
#         Coding Interview Question
#
#                 URLIFY
#  Write a method to replace all spaces
#  in a string with '%2e'
#  
#  >> Input: "Mr John Smith"
#  >> Output: "Mr%20John%20Smith"
#  
# Question 1.3 | ctci 6th edition
#
#  by: @estalvgs1999
# --------------------------------------

# Complexity => O(n)
def urlify(string):
    return '%20'.join(string.split())


if __name__ == "__main__":
    
    s_input = "Mr John Smith"
    print(urlify(s_input))
    


    