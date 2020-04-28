# Function that runs tests to function
from first_non_repeating_char import *
from termcolor import colored
import unittest

test_arrays =[  ('aaswweeeaadssdffcv','c'),
                ('bbcdecdefghijklmnfopqrstuvwxyz','g'),
                ('asvsav','_'),
                ('','_'),
                ('aa','_'),
                ('abbca','c'),
                ('xxmjmnhhbjgtyikbjhsvcaj','n'),
                ('estebanalvaradovargas','t'),
                ('zzzxxxzxzxzxzx','_'),
                ('qscvhuqscihb','v')]

    
def bf_test():
    
    correct = 0

    print('\nBRUTE FORCE SOLUTION TESTING\n'+'-'*30)

    for test in test_arrays:
        ans = bf_first_non_repeating_character(test[0])
 
        if ans.__eq__(test[1]):
            print(colored('TEST ------------> OK','green'))
            correct += 1
        else:
            print(colored('TEST ------------> FAIL','red'))
            print(colored('Test: {0}\nExpected Output {1} \nYour Output:{2}'.format(test[0],test[1],ans),'red'))

    print('🆗',colored('{0}/{1} tests passed'.format(correct,len(test_arrays)),'green'))

def hm_test():
    
    correct = 0

    print('\nHASH MAP SOLUTION TESTING\n'+'-'*30)

    for test in test_arrays:
        ans = hm_first_non_repeating_character(test[0])
 
        if ans.__eq__(test[1]):
            print(colored('TEST ------------> OK','green'))
            correct += 1
        else:
            print(colored('TEST ------------> FAIL','red'))
            print(colored('Test: {0}\nExpected Output {1} \nYour Output:{2}'.format(test[0],test[1],ans),'red'))

    print('🆗',colored('{0}/{1} tests passed'.format(correct,len(test_arrays)),'green'))

def ln_test():
    
    correct = 0

    print('\nLINEAR SOLUTION TESTING\n'+'-'*30)

    for test in test_arrays:
        ans = first_non_repeating_character(test[0])
 
        if ans.__eq__(test[1]):
            print(colored('TEST ------------> OK','green'))
            correct += 1
        else:
            print(colored('TEST ------------> FAIL','red'))
            print(colored('Test: {0}\nExpected Output {1} \nYour Output:{2}'.format(test[0],test[1],ans),'red'))

    print('🆗',colored('{0}/{1} tests passed'.format(correct,len(test_arrays)),'green'))


def run_test():
    bf_test()
    hm_test()
    ln_test()
