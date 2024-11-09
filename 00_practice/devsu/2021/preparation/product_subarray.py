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
        [-3, 4, 7, 5, -2, -2],
        [-4, 3, 2, -2, -150, 4],
        [1, -10, -5, -100, 200],
    ]
    expected = [
        [-3, 4, 7, 5, -2],
        [3, 2, -2, -150, 4],
        [-5, -100, 200],
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

def solve_inefficient(array):
    n = len(array)

    max = -math.inf
    max_i = 0
    max_j = 1
    for i in range(n-1):
        multiplier = array[i]
        for j in range(i+1, n):
            multiplier *= array[j]
            if multiplier > max:
                max = multiplier
                max_i = i
                max_j = j

    return array[max_i:max_j+1]

# kadane only work for sum, so lets use a variation
def solve(array):
    # using kadane's algorithm

    n = len(array)

    if n == 1:
        return array


    min_current = array[0]
    max_current = array[0]

    min_related_array = [array[0]]
    max_related_array = [array[0]]

    max_answer = [array[0]]
    min_answer = [array[0]]

    for i in range(1, n):
        value = array[i]
        value_with_min = value * min_current
        value_with_max = value * max_current

        maximum = max(value, value_with_min, value_with_max)
        minimum = min(value, value_with_min, value_with_max)


        holder_min = copy.deepcopy(min_related_array)
        holder_max = copy.deepcopy(max_related_array)



        if maximum == value:
            # reset
            max_related_array = [value]
        elif maximum == value_with_min:
            max_related_array = holder_min
            max_related_array.append(value)

        elif maximum == value_with_max:
            max_related_array.append(value)


        if minimum == value:
            # reset
            min_related_array = [value]
        elif minimum == value_with_min:
            min_related_array.append(value)

        elif minimum == value_with_max:
            min_related_array = holder_max
            min_related_array.append(value)




        if maximum > max_current:
            max_current = maximum
            max_answer = max_related_array
            
        if minimum < min_current:
            min_current = minimum
            min_answer = min_related_array

        

    return max_answer


if debug:
    test()