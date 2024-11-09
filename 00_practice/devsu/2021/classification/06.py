
import traceback
import time
import random
import sys
import copy
sys.setrecursionlimit(10000000)



debug = True

def test():

    test_cases = [
        [3, 3],
        [1, 3],
        [7, 8],
        [9, 9],

    ]
    expected = [24, 3,  -1, -1]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i][0], test_cases[i][1])

            print(solution)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")

import math

def tree(actual, u, max_level, level):

    if level == max_level:
        return 1

    sum = 0
    for i in range(1, u+1):
        element = str(i)
        if len(actual) >= 2:
            if actual[-1] == element and actual[-2] == element:
                # cant, next
                continue

        new_actual = actual + element
        sum = sum + tree(new_actual, u, max_level, level+1)
    
    return sum


    

def solve(size, u):
    answer = tree("", u, size, 0)
    return answer



if debug:
    test()