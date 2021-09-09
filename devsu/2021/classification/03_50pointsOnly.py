
import traceback
import time
import random
import sys
import copy
sys.setrecursionlimit(10000000)



debug = True

def test():

    test_cases = [
        1, 6, 77, 545421,
        81239812739128371,
        87123641123172368,
        9223372036854775807,
    ]
    expected = [1, 4, 39, 272711, 40619906369564187, 43561820561586186, 4611686018427387903]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])

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
def solve(n):
    # pattern ->
    q = math.floor((n-1)/4)
    return n - 2 * q





if debug:
    test()
