import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)

debug = True

def test():

    test_cases = [
        14,
        4,
        7,
        13,
    ]
    expected = [
        "(-(-_-(-_(-_(-_-(-_(-_(-_-)_-)_-)-_-)_-)_-)-)",
        "(-_(-_(-_-)_-)",
        "",
        ""]
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


def solve(num):

    guys = {
        "complete": "(-_-)",
        "side_left": "(-_",
        "side_right": "_-)",
        "partial_left": "(-_-",
        "partial_right": "-_-)",
        "final_left": "(-",
        "final_right": "-)",
    }

    answer = guys["complete"]

    total_iter = num-1

    if num > 7:
        total_iter -= 2

    left_count = 0
    right_count = 0

    turn = 1
    for i in range(total_iter):
        if turn == 0:
            right_count += 1

            if right_count % 3 == 0:
                answer += guys["partial_right"]
            else:
                answer += guys["side_right"]
            turn = 1

            

        else:
            
            left_count += 1
            
            if left_count % 3 == 0:

                answer = guys["partial_left"] + answer
            else:
                answer = guys["side_left"] + answer
            turn = 0

    if num > 7:
        answer = guys["final_left"] + answer + guys["final_right"]

    # print(answer)
    return answer

    

if debug:
    test()

