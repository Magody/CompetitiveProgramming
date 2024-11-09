import copy
from typing import List

class Solution:
    def lengthOfLIS(self, nums):
        
        n = len(nums)
        dp = [1 for _ in range(n)]
        
        for i in range(n-2, -1, -1):

            for j in range(i+1, n):

                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])

        return max(dp)





        


def test():
    test_cases = [
        [10,9,2,5,3,7,101,18],
        [1,2,4,3],
    ]
    expected = [
        4,
        3,
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