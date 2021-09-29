

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:  
        
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    
    
    def helper(self,nums):
    
        rob1,rob2=0,0
    
        for n in nums:
           newRob=max(rob1+n,rob2)
           rob1=rob2
           rob2=newRob
        
        return rob2
    
def test():
    test_cases = [
        [2, 3, 2],[1,2,3,1]
    ]
    expected = [
        3,4
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = Solution().rob(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test()