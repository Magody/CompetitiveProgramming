import math
import traceback
import time
import random
import sys
from typing import DefaultDict
sys.setrecursionlimit(10000000)



debug = False

def test():

    test_cases = [
        {
            's': 'xaybaba' * 1,
            'q': 1,
            'queries': ['aaba', 'yx']
        },

    ]
    expected = [[4, 1]]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            s = test_cases[i]["s"]
            q = test_cases[i]["q"]

            solution = solve(s, q)

        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def binary_search_greater_than(array, n, target, level = 0):
    # bisect is faster
    if n <= 0:
        return -1
    
    mid = math.floor(n/2)
    pivot = array[mid]
    if pivot > target:
        if mid - 1 >= 0 and array[mid-1] <= target:
            return array[mid]
        elif n == 1:
            return array[mid]
        else:
            return binary_search_greater_than(array[:mid], mid, target, level + 1)
    else:
        return binary_search_greater_than(array[mid+1:], n - mid - 1, target, level + 1)
    

# res = binary_search_greater_than([0,3,17], 3, -17)
# print(res)

def normal_search(array, n, minimum_index):
    if n == 0:
        return -1, -1

    for i in range(n):
        if array[i] > minimum_index:
            return array[i], i
    return -1, -1
    

import bisect


def solve(s, q):
    len_s = len(s)

    preprocess = DefaultDict(list) #  dict() {letter:[i] for i, letter in enumerate(s)}

    for index in range(len_s -1, -1 ,-1):
        preprocess[s[index]].append(len_s-(index+1)) 
        


    for _ in range(q):
        # query = "yx" # "aaba"
        query = input()
        
        len_query = len(query)

        pq = len_query-1

        minimum_index = -2
        answer = 0

        while pq >= 0:

            letter = query[pq]
            
            if letter in preprocess:

                array = preprocess[letter]

                index = bisect.bisect_left(array, minimum_index+1)
                minimum_index = -1
                try:
                    minimum_index = array[index]
                except:
                    pass

                # res, index = normal_search(array, len(array), minimum_index)
                
                # preprocess[letter] = preprocess[letter][index+1:]
                # res = binary_search_greater_than(array, len(array), minimum_index)

                if minimum_index == -1:
                    break
                else:
                    # preprocess[letter] = array[index:]
                    answer += 1

            else:
                break

            pq -= 1
        
        print(answer)

    

if debug:
    test()
else:
    s = input()
    q = int(input())
    try:

        res = solve(s, q)
    except Exception as error:
        # check if exist error
        # time.sleep(3)
        for _ in range(q):
            print("Error: ", error)

