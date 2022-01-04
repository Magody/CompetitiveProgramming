

def cond_one(nums, i):

    condition = True

    for j in range(0, i):
        
        for k in range(i+1,len(nums)):

            if nums[j] < nums[i] and nums[i] < nums[k]:
                pass
            else:
                return False

    return condition

def cond_two(nums, i, last_cond):

    if last_cond:
        return False

    return nums[i - 1] < nums[i] and nums[i] < nums[i + 1]



nums = [2,4,6,4]

for i in range(1, len(nums)-1):
    res = 0

    if cond_one(nums, i):
        res = 2

    elif cond_two(nums, i, False):
        res = 1

    print(res)