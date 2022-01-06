# https://codeforces.com/problemset/problem/546/A

def myFunction():
    inp = input().split()
    k = int(inp[0]) 
    n = int(inp[1]) 
    w = int(inp[2])
    #Formula for Sum of Arithmetic Sequence Formula
    #S = n⁄2 {2a + (n − 1) d}
    #https://byjus.com/sum-of-arithmetic-sequence-formula/
    totalCost = ((w/2)*(2*k + (w-1)*k))
    amount = int(totalCost - n)
    if amount < 0:
        print(0)
    else:
        print(amount)


myFunction()