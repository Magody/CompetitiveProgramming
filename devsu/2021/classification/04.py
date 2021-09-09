
import traceback
import time
import random
import sys
import copy
sys.setrecursionlimit(10000000)



debug = True

def test():

    test_cases = [
        ["AB", 5],
        ["ABC", 4],
        ["ABCD", 83],
        ["MNOQ", 22421],
        ["OQWUEFQWUEFIUFGEW", 65465478],

    ]
    expected = ["BB", "AB",  "DDD",  "MMMONMMN", "QIOUEQU"]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i][0], test_cases[i][1])

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

def tree(letters, n, actual_letters, counter = [0], level = 0, queue = []):

    len_letters = len(letters)
    len_actual_letters = len(actual_letters)


    while counter[0] <= n:

        element = queue.pop(0)

        for letter in letters:
            queue.append(element + letter)
            counter[0] += 1

            if counter[0] == n + 1:
                break



        # print()

    return queue[-1]


def solve(letters, n):

    return getNameFromNumber(letters, n+1)

def getNameFromNumber(text, num):
    
    len_text = len(text)
    numeric = (num-1) % len_text
    letter = text[numeric]
    num2 = math.floor((num-1) / len_text)
    if (num2 > 0) :
        return getNameFromNumber(text, num2) + letter
    else:
        return letter
    
# print(getNameFromNumber(22+1))

def solve_brute_force(letters, n):


    queue = []
    
    for letter in letters:
        queue.append(letter)



    answer = tree(letters, n, "", [len(letters)], 0, queue)
    return answer


if debug:
    test()