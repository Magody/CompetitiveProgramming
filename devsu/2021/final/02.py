import math

def tree(jumps, index, target, level = 0):

    if index > target:
        return None
    if index == target:
        return True

    value = jumps[index]

    answer = None

    for i in range(1, value+1):

        answer = tree(jumps, index+i, target, level+1)
        if answer is not None:
            return answer

    return answer
        





def solve(jumps):
    len_jumps = len(jumps)

    answer = tree(jumps, 0, len_jumps-1)
    
    return answer == True

# [3,1,1,1]
# [1,0,1]
# 
# 
print(solve([2,5,5,2,5,3,4,0,5,1,0,4,3,2,0,1,1,4,3,0,2,3,1,5,3,5,2,2,1,5,2,5,4,2,4,2,4,0,3,5,2,1,5,1,0,0,4,3,2,4,4,5,0,3,1,4,0,2,1,4,1,0,4,3,5,5,1,5,4,0,2,1,5,2,4,3,5,2,1,2,0,5,2,4,2,1,2,4,5,4,1,0,0,3,3,5,2,0,0,0]))
print(solve([1,2,2,5,2,5,2,5,5,4,4,4,4,4,2,4,0,3,3,3,4,2,4,3,2,3,5,0,3,4,2,2,1,1,3,5,2,2,4,4,1,4,1,3,5,3,1,3,1,5,2,0,3,5,5,2,4,0,4,3,1,4,5,0,3,4,5,2,4,5,4,4,1,5,0,4,5,0,5,2,0,5,0,3,3,4,1,5,3,4,1,1,1,2,5,0,3,5,2,1]))