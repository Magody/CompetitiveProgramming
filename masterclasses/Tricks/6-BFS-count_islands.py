import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)


debug = True

def test():
    test_cases = [
        [
            # []
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1],
        ],
        [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1],
        ],

    ]
    expected = [
        2, 7
    ]
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


def BFS(matrix, i, j, r, c):
    up = i - 1
    right = j + 1
    down = i + 1
    left = j - 1

    directions = []

    if up >= 0 and matrix[up][j] == 1:
        matrix[up][j] = 0
        directions.append([up, j])
    if right < c and matrix[i][right] == 1:
        matrix[i][right] = 0
        directions.append([i, right])
    if down < r and matrix[down][j] == 1:
        matrix[down][j] = 0
        directions.append([down, j])
    if left >= 0 and matrix[i][left] == 1:
        matrix[i][left] = 0
        directions.append([i, left])
    matrix[i][j] = 0
    return directions

def solve(matrix):
    islands = 0
    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        for j in range(c):

            element = matrix[i][j]

            # zero is not important
            if element == 1:
                q = [[i, j]]

                while len(q) > 0:

                    directions = BFS(matrix, q[0][0], q[0][1], r, c)
                    q.pop(0)
                    q.extend(directions)
                islands += 1



    
    
    return islands
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

