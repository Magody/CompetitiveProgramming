import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)



debug = False

def test():
    limit_r = 200
    limit_c = 200
    limit_example = [[0 for _ in range(limit_c)] for _ in range(limit_r)]

    for i in range(limit_r):
        for j in range(limit_c):
            limit_example[i][j] = -1000
    limit_example[0][0] = 0
    limit_example[limit_r-1][limit_c-1] = 0
    answer_limit = 397001

    test_cases = [
        {
            "r": 3, "c": 3,
            "matrix": [
                [0, 1, 2],
                [-2, -9, -4],
                [-8, 5, 0]
            ]
        },
        {
            "r": 2, "c": 2,
            "matrix": [
                [0, -2],
                [2, 0]
            ]
        },
        {
            "r": 5, "c": 6,
            "matrix": [
                [0, 1, 2, 3, -1, -1],
                [-3, -1, -1, 4, -1, -1],
                [-2, -1, -1, 5, 6, -1],
                [-10, -1, -1, -5, 10, -100],
                [-4, 50, 20, 2, -80, 0],
            ]
        },
        {
            "r": 3, "c": 4,
            "matrix": [
                [0, -1000, 1000, -1000],
                [0, 0, -1000, -100],
                [0, 10, -11, 0],
            ]
        },
        {
            "r": limit_r, "c": limit_c,
            "matrix": limit_example
        },
        {
            "r": 6, "c": 6,
            "matrix": [
                [+000, +100, +100, +100, +200, +100],
                [-100, -100, -100, -100, -100, -100],
                [-100, -100, -100, -100, -100, -100],
                [-100, -100, -100, -100, -100, +300],
                [+900, -100, -100, -100, -100, -854],
                [+200, -100, -100, -100, -937, +000],
            ]
        },
        {
            "r": 3, "c": 3,
            "matrix": [
                [+000, -100, +100],
                [-100, +100, +000],
                [+100, +000, +000],
            ]
        },

    ]
    expected = [2, 1,  11, 2, answer_limit, 155, 1]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            r = test_cases[i]["r"]
            c = test_cases[i]["c"]
            matrix = test_cases[i]["matrix"]
            solution = solve(r, c, matrix)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def gotcha(r, c, matrix, i, j, cost, memo, level = 0):

    if i == r-1 and j == c - 1:
        # we reach the end solution
        return 0
    if i >= r or j >= c:
        # Out of grid
        return -math.inf

    key = f"{i},{j}"
    if key in memo:
        return memo[key]
        

    new_cost = cost + matrix[i][j]
    

    cost_down = gotcha(r, c, matrix, i+1, j, new_cost, memo, level+1)
    cost_right = gotcha(r, c, matrix, i, j+1, new_cost, memo, level+1)


    memo[key] = matrix[i][j] + max(cost_down, cost_right)
    
    

    return memo[key]

def solve(r, c, matrix):
    
    answer = gotcha(r, c, matrix, 0, 0, 0, dict())

    if debug:
        print("Total answer: ", answer)
    if answer >= 0:
        return 1
    
    return 1 - answer

if debug:
    test()
else:
    try:

        r, c = map(int, input().split(" "))
        matrix = [list(map(int, input().split(" "))) for _ in range(r)]
        print(solve(r, c, matrix))
    except Exception as error:
        # check if exist error
        time.sleep(3)
        print("Error: ", error)

