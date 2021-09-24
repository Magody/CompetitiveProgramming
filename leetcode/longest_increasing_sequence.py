import copy
from typing import List

class Solution:
    def lengthOfLIS(self, nums):
        
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[n-1] = 1  # base case

        
        for i in range(n-2, -1, -1):

            maximum = 0
            for j in range(i+1, n):

                lis_i_plus_1 = 0
                if nums[i] < nums[j]:
                    lis_i_plus_1 = 1

                dp[i] = 1 + max(lis_i_plus_1, maximum)

                if dp[i] > maximum:
                    maximum = dp[i]

        return dp[0]





        


def test():
    test_cases = [
        [10,9,2,5,3,7,101,18]
    ]
    expected = [
        4
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = Solution().lengthOfLIS(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test() # test()