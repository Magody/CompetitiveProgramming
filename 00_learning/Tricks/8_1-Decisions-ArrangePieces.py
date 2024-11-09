import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)



debug = True

def test():
    

    test_cases = [
        4, 5
    ]
    expected = [11, 24]
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

def tree_pieces(n, filled_horizontal, memo, level):

    # Base case
    if filled_horizontal == n:
        return 1  # collect path
    
    if filled_horizontal > n:
        return 0  # impossible path

    if filled_horizontal in memo:
        # dynamic programming
        return memo[filled_horizontal]

    total_first_shape_2x1 = tree_pieces(n, filled_horizontal+1, memo, level + 1)
    total_first_shape_2x2 = tree_pieces(n, filled_horizontal+2, memo, level + 1)
    
    available_space = n - filled_horizontal
    # L pair case 1:
    total_L_case_1 = 0
    limit_L_case_1 = math.floor((available_space-3)/2)
    i = 0
    while i <= limit_L_case_1:
        filled_L_case_1 = 3 + i*2
        total_L_case_1 = total_L_case_1 + tree_pieces(n, filled_horizontal+filled_L_case_1, memo, level + 1)
        i += 1
    total_L_case_1 *= 2  # exist mirror case for this, so multiply by two

    # L pair case 2:
    total_L_case_2 = 0
    limit_L_case_2 = math.floor((available_space-2)/2)
    j = 1
    while j <= limit_L_case_2:
        filled_L_case_2 = 4 + (j-1) * 2
        total_L_case_2 = total_L_case_2 + tree_pieces(n, filled_horizontal+filled_L_case_2, memo, level + 1)
        j += 1
    total_L_case_2 *= 2  # exist mirror case for this, so multiply by two

    memo[filled_horizontal] = total_first_shape_2x1 + total_first_shape_2x2 + total_L_case_1 + total_L_case_2

    return memo[filled_horizontal]

def solve(n):

    if n <= 0:
        return 0

    return tree_pieces(n, 0, dict(), 0)


if debug:
    test()