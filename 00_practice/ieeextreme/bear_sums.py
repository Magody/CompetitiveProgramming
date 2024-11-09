import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)


debug = True

def test():

    test_cases = [
        {
            "target": 8, "length": 4,
            "array": [1, 2, 4, 4]
        },
        {
            "target": 8, "length": 4,
            "array": [1, 2, 7, 9]
        },
        {
            "target": 8, "length": 4,
            "array": [1, 2, 8, 9]
        },
        {
            "target": 8, "length": 4,
            "array": [4, 5, 3, 4]
        },
        {
            "target": 8, "length": 4,
            "array": [4, 1, 1, 8]
        },
        {
            "target": 8, "length": 4,
            "array": [-1, 1, 9, 8]
        },



    ]
    expected = [
        "4 4", 
        "1 7", "!OK", "3 5", "!OK", "-1 9"
    ]

    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            target = test_cases[i]["target"]
            length = test_cases[i]["length"]
            array = test_cases[i]["array"]
            solution = solve(array, target, length)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def solve(array, target, length):
    out = "!OK"
    # [1 2 4 4]
    # {1, 2, 4,  }
    myset = set()
    for num in array:

        diff = target - num
        if diff in myset:
            resultado = sorted([diff, num])
            out = str(resultado[0]) + " " + str(resultado[1])
            break
        else:
            myset.add(num)

    return out


if debug:
    test()
else:
    try:
        t = int(input())
        for _ in range(t):
            target, length = map(int, input().split(" "))
            if length == 0:
                print("!OK")
                input()
                continue

            array = map(int, input().split())
            print(solve(array, target, length))
    except Exception as error:
        # check if exist error
        time.sleep(3)
        print("Error: ", error)





    
