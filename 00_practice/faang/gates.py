import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)

# 20 min

debug = True

def areMatrixEqual(matrix1, matrix2):

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True
def test():
    
    inf = math.inf
    test_cases = [
        [
            [inf, -1, 0, inf],
            [inf, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf],
        ],
        [
            [inf, -1, 0, inf],
            [-1, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf],
        ],

    ]
    expected = [
        [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
        [
            [inf, -1, 0, 1],
            [-1, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
    ]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])

            assert areMatrixEqual(solution, expected[i])
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def fillMatrixFromGate(matrix, index, m, n, step = 0, visited = [], level = 0):
    # DFS function

    i = index[0]
    j = index[1]

    if index not in visited:
        if i - 1 >= 0:
            if matrix[i-1][j] == math.inf or (matrix[i-1][j] != 0 and matrix[i-1][j] >= step + 1):
                matrix[i-1][j] = step + 1
                fillMatrixFromGate(matrix, [i-1, j], m, n, step + 1, visited, level + 1)
                visited.append([i-1, j])


        if i + 1 < m:
            if matrix[i+1][j] == math.inf or (matrix[i+1][j] != 0 and matrix[i+1][j] >= step + 1):
                matrix[i+1][j] = step + 1
                fillMatrixFromGate(matrix, [i+1, j], m, n, step + 1, visited, level + 1)
                visited.append([i+1, j])

        if j - 1 >= 0:
            if matrix[i][j-1] == math.inf or (matrix[i][j-1] != 0 and matrix[i][j-1] >= step + 1):
                matrix[i][j-1] = step + 1
                fillMatrixFromGate(matrix,[i, j-1], m, n, step + 1, visited, level + 1)
                visited.append([i, j-1])


        if j + 1 < n:
            if matrix[i][j+1] == math.inf or (matrix[i][j+1] != 0 and matrix[i][j+1] >= step + 1):
                matrix[i][j+1] = step + 1
                fillMatrixFromGate(matrix, [i, j+1], m, n, step + 1, visited, level + 1)
                visited.append([i, j+1])


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    indexes = []
    # O(m*n)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # is gate
                indexes.append([i, j])

    for index in indexes:
        fillMatrixFromGate(matrix, index, m, n, 0, [])

    return matrix

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

