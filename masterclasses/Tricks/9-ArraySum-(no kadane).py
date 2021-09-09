import copy
from typing import List
import pytest

def solve(array: List):

    sum_holder = copy.deepcopy(array)
    displacement = 0
    count_until_zero = 0
    last_limit = 0
    final_array = []

    while len(sum_holder) > 1:
        count_until_zero += 1

        displacement+=1
        preserve = False
        for j in range(len(sum_holder)-1):
            real_index = j+displacement
            sum_holder[j] = sum_holder[j] + array[real_index]
            if sum_holder[j] == 0:
                final_array.extend(array[last_limit:real_index-count_until_zero])
                last_limit = real_index + 1
                displacement = last_limit # count_until_zero + (j - 1)
                count_until_zero = 0
                sum_holder = array[real_index+1:]
                preserve = True
                break
        if not preserve:
            sum_holder.pop()
    final_array.extend(sum_holder)
    return final_array

def test():
    test_cases = [
        [2, -2, 3, 3, -4, 7, -6, 1],
        [2, -2, 3, -4, 7, -6],
        [2, -2, 3, -4, 7, -6, 1],
        [1, 3, 4, -7, 5, -6, 2, 5, -1, 8],
        [1, 2, 2, 3, -5, 3, 4,5, -6, 1, -9],
        [1, -1],
        []
    ]
    expected = [
        [3, 1],
        [],
        [1],
        [1, 5, 8],
        [1, 2, 3, 4, -9],
        [],
        []
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test()