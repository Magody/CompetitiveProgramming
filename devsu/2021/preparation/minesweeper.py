import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)


debug = True

def test():

    x = "x"
    test_cases = [
        [
            ["", "", "", x, "", "", "", x, "", ""],
            ["", "", x, "", "", x, "", "", "", x],
            ["", x, "", "", "", x, x, x, x, ""],
            ["", "", "",x, "", x, "", x, "", ""],
            ["", "", "", "", "", x, x, x, "", x],
            ["", x, "", "", x, x, x, "", "", ""]
        ],

    ]
    expected = [
        [
            ["0","1","2",x,"2","1","2",x,"2","1"],
            ["1","2",x,"2","3",x,"5","4","4",x],
            ["1",x,"3","2","4",x,x,x,x,"2"],
            ["1","1","2",x,"4",x,"8",x,"5","2"],
            ["1","1","2","2","5",x,x,x,"3",x],
            ["1",x,"1","1",x,x,x,"3","2","1"]
        ]
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


def convertIntOr0(value):
    if value == "":
        return 0
    return int(value)

def addBombAround(matrix, i, j, m, n):

    up = i - 1
    right = j + 1
    down = i + 1
    left = j - 1
    can_add_up = up >= 0
    can_add_right = right < n
    can_add_down = down < m
    can_add_left = left >= 0

    ## UP
    if can_add_up:
        if matrix[up][j] != "x":
            matrix[up][j] = str(convertIntOr0( matrix[up][j]) + 1)

        ## UP - RIGHT
        if can_add_right and matrix[up][right] != "x":
            matrix[up][right] = str(convertIntOr0(matrix[up][right]) + 1)
        ## UP - LEFT
        if can_add_left and matrix[up][left] != "x":
            matrix[up][left] = str(convertIntOr0(matrix[up][left]) + 1)

    ## DOWN
    if can_add_down:
        if matrix[down][j] != "x":
            matrix[down][j] = str(convertIntOr0( matrix[down][j]) + 1)
        ## DOWN - RIGHT
        if can_add_right and matrix[down][right] != "x":
            matrix[down][right] = str(convertIntOr0(matrix[down][right]) + 1)
        ## DOWN - LEFT
        if can_add_left and matrix[down][left] != "x":
            matrix[down][left] = str(convertIntOr0(matrix[down][left]) + 1)

    # SIDES
    if can_add_right and matrix[i][right] != "x":
        matrix[i][right] = str(convertIntOr0(matrix[i][right]) + 1)
    if can_add_left and matrix[i][left] != "x":
        matrix[i][left] = str(convertIntOr0(matrix[i][left]) + 1)





def solve(matrix = None):

    if matrix == None:
        return None

    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            element = matrix[i][j]

            if element == "x":
                # sum around
                addBombAround(matrix, i, j, m, n)
            elif element == "":
                matrix[i][j] = "0"
    
    
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

