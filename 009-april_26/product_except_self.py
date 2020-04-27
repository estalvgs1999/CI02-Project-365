# ---------------------------------------
#                   DAY 9
#         Apple Interview Question
#
#            PRODUCT EXCEPT SELF
#  Given an array nums of n integers where
#  n > 1, return an array such that out[i]
#  is equal to the product of all elements
#  except nums[i].
#
#  Input/Output array must be sorted
#  by: @estalvgs1999
# ----------------------------------------

# Brute Force Solution
# Complexity O(n²)
def bf_product_except_self(nums):

    output = []

    for i in range(len(nums)):
        current_product = 1
        for j in range(len(nums)):
            if i != j:   
                current_product *= nums[j]
        output.insert(i,current_product)

    return output

# Using division Solution 
# Complexity O(2n)
def ud_product_except_self(nums):

    p = 1
    for n in nums: p*=n
    output = [p//n for n in nums]
    
    return output

# Solution without division
# Complexity O(3n)
def wd_product_except_self(nums):

    n = len(nums)
    output = [None]*n
    left_p,rigth_p = [1]*n, [1]*n

    for i in range(1,n):
        left_p[i] = nums[i-1]*left_p[i-1]

    for i in range(n-2,-1,-1):
        rigth_p[i] = nums[i+1]*rigth_p[i+1]

    for i in range(n):
        output[i] = rigth_p[i]*left_p[i]

    return output

if __name__ == "__main__":
    print(bf_product_except_self([1,2,3,4]))
    print(ud_product_except_self([1,2,3,4]))
    print(wd_product_except_self([1,2,3,4]))