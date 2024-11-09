import copy
from typing import List

class Solution:
    def trap(self, heights: List):
        p1 = 0
        p2 = len(heights) - 1
        maxL = 0
        maxR = 0
        area_total = 0
        while p1 != p2:
            # A = 1 * (min(maxL, maxR) - heights[i])
            height_in_p1 = heights[p1]
            height_in_p2 = heights[p2]
            # updating max height
            if height_in_p1 > maxL:
                maxL = height_in_p1
            if height_in_p2 > maxR:
                maxR = height_in_p2

            if height_in_p1 <= height_in_p2:
                # get area in this point
                area_total += min(maxL, maxR) - height_in_p1
                p1 += 1
            else:
                area_total += min(maxL, maxR) - height_in_p2
                p2 -= 1
        return area_total


        


def test():
    test_cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [3,0,0,2,1,2],
        [4,2,0,3,2,5]
    ]
    expected = [
        6,
        5,
        9
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = Solution().trap(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

# test() # test()