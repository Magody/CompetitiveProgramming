import math
import traceback
import time
import random
import sys
import copy
sys.setrecursionlimit(10000000)



debug = True

def test():

    test_cases = [
        [-1, 3, -5, 7, 8, 8, -1],
        [1, 1, 2, 3, 4, 5, 5, 5, 6],
        [2,-10,0,-8,4,-5,10,0,8,-9,4,-6,3,4,8,10,6,-5,2,-6,9,-10,4,-1,6,-1,7,10,-10,-3,-6,1,7,-1,9,-1,2,3,4,8,-3,-3,-5,5,-8,-1,9,8,8,0,-5,3,-6,-9,10,-8,-3,-4,-1,-8,-6,4,-10,1,7,-1,0,10,1,-1,-6,-2,-2,5,-1,-7,4,5,-5,6,-7,6,-2,-5,5,7,-4,8,0,8,-10,-7,-2,0,9,10,5,5,-8,9],
        [4,-10,6,-3,-2,-4,-9,10,0,-7,-4,-9,-4,2,-6,-7,10,1,8,10,5,1,2,-8,2,-10,0,-6,4,-2,-6,8,-3,0,9,-4,4,-5,4,-8,-1,-3,-8,8,-6,-7,8,6,0,9,2,-3,-4,4,-5,-2,0,3,0,-3,-6,-4,1,-4,-5,3,2,1,4,-8,-8,-3,-6,2,-4,9,-6,-9,0,9,9,-6,3,-4,0,-7,-5,0,6,-6,-10,4,-2,6,-3,-1,4,1,-3,-7],


    ]
    expected = [-5, 2, -10, -6,]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])

            # print(solution)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def solve(array):
    
    memo = {}
    total_sum = 0

    for i in range(len(array)):
        element = array[i]
        if element in memo:
            memo[element] = memo[element] + element
        else:
            memo[element] = element

        total_sum += element

    best_number = array[0]
    best_sum = -math.inf

    for key, value in memo.items():

        sum_different = total_sum - value

        if sum_different > best_sum:
            best_sum = sum_different
            best_number = key
        elif sum_different == best_sum and key > best_number:
            best_number = key
            best_sum = sum_different

    
    return best_number





if debug:
    test()