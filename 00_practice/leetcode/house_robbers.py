import copy
from typing import List

class Solution:
    def rob(self, nums: List):
        len_nums = len(nums)
        dp = [0 for _ in range(len_nums)]
        dp[len_nums-1] = nums[len_nums-1]

        for i in range(len_nums-2, -1, -1):
            value = 0
            if i+2 < len_nums:
                value = dp[i+2]
            dp[i] = max(nums[i] + value, dp[i+1])
        print(dp)
        return dp[0]


        


def test():
    test_cases = [
        [2, 8, 4, 2, 5]
    ]
    expected = [
        13
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = Solution().rob(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test() # test()