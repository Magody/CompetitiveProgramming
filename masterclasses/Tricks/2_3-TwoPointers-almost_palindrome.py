import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)



debug = True

def test():

    

    test_cases = [
        "raceacar",
        "Abccdba",
        "Abcdefdba",
        "",
        "A",
        "Ab"

    ]
    expected = [True, True, False, True, True, True]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            
            solution = isAlmostPalindrome(test_cases[i])

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")



def isAlmostPalindrome(word):

    word = word.lower()

    p1 = 0
    p2 = len(word)-1

    max_removing = 1

    while p1 <= p2:

        if word[p1] != word[p2]:
            if max_removing == 0:
                return False
            max_removing -= 1
            if word[p1+1] == word[p2]:
                p1 += 1
            elif word[p2-1] == word[p1]:
                p2 -= 1
            continue


        p1 += 1
        p2 -= 1
    
    return True

if debug:
    test()

