

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if (len(s1)+len(s2)!=len(s3)):
            return False
        
        dp = [[False]*(len(s2)+1) for i in range (len(s1)+1)]
        
        dp [len(s1)][len(s2)]=True
        
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i < len(s1) and s1[i]==s3[i+j] and dp [i+1][j]:
                    dp[i][j]=True
                if j < len(s2) and s2[j]==s3[i+j] and dp [i][j+1]: 
                    dp[i][j]=True
                    
        return dp[0][0]

def test():
    test_cases = [
        ["aabcc","dbbca","aadbbcbcac"],["aabcc","dbbca","aadbbbaccc"],
        ["","",""]
    ]
    expected = [
        True,False,True
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = Solution().isInterleave(test_cases[i][0],test_cases[i][1],test_cases[i][2])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test()