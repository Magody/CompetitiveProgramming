import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)



debug = True

def test():

    

    test_cases = [
        [10, 15, 30],
        [10, 50, 2, 1, 8, 9],
        [20, 15, 10, 30, 12, 4, 3],
        [10, 20, 10, 5, 3, 1, 40, 80, 70],
    ]
    expected = [15, 20, 40, 104]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            
            solution = solve(test_cases[i])

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def tree(vector, n, stair, level, memo):

    if stair in memo:
        return memo[stair]

    if stair > n:
        return 0
    
    actual_cost = 0
    if stair > 0:
        actual_cost = vector[stair-1]

    res_one_step = tree(vector, n, stair+1, level+1, memo)
    res_two_step = tree(vector, n, stair+2, level+1, memo)

    memo[stair] = actual_cost + min(res_one_step, res_two_step)
    return memo[stair]

def solve(vector):

    answer = tree(vector, len(vector), 0, 0, {})

    return answer

    

if debug:
    test()

