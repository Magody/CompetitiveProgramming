import math

t = int(input())

out = ""
for i in range(t):

    def op(a,b,x):
        return (a ^ x) + (b ^ x)

    a, b = map(int, input().split(" "))


    x = a & b


    best = op(a,b,x)
    
    if i < t-1:
        out += f"{best}\n"
    else:
        out += f"{best}"
        
print(out)
