"""
:param k int cost of the first banana
:param n int number of dollars the soldier has
:param w int number of bananas he wants
"""
def solve():
    test_case = input().split(" ")
    
    k,n,w = [int(i) for i in test_case]
    
    total_to_pay = k * w * (w + 1) / 2

    if total_to_pay <= n:
        return 0

    dollars_to_borrow = total_to_pay - n

    return int(dollars_to_borrow)

print(solve())
