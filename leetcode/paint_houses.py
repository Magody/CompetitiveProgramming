import copy
from typing import List

class Solution:
    def minCost(self, costs_matrix):
        rows = len(costs_matrix)
        if rows == 0:
            return 0
        cols = len(costs_matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        dp[0] = costs_matrix[0]

        for i in range(1, rows):
            dp[i][0] = costs_matrix[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs_matrix[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs_matrix[i][2] + min(dp[i-1][0], dp[i-1][1])

        return min(dp[rows-1])



        


def test():
    test_cases = [
        [[17, 2, 17], [2, 10, 6], [1, 30, 3]]
    ]
    expected = [
        7
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = Solution().minCost(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test() # test()