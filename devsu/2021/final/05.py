import math
import copy

def tree(indexes, source, target, offset, sum = [0], level = 0, memo = {}):
    len_source = len(source)
    len_target = len(target)



    if len_source == len_target:
        if source == target:
            sum[0] += 1
            return 1
        else:
            return 0
        
    elif len_source < len_target:
        
        return 0


   

    for i in range(len_source):
        new_source = source[:i] + source[i+1:]

        new_indexes = copy.deepcopy(indexes)
        new_indexes.pop(i)
        
        new_p = copy.deepcopy(new_indexes)
        new_p.sort()
        key = ""
        for r in new_p:
            key += f"{r}-"



        if key not in memo:
            tree(new_indexes, new_source, target, i + 1, sum, level + 1, memo)
        
            memo[key] = 1
        else:
            pass

        


def solve(source, target):

    indexes = [i for i in range(len(source))]
    sum = [0]
    tree(indexes, source, target, 0, sum)

            





    
    
    return sum[0]
    
# [1,2,7,4,2,5]
# 
# 
# 
print(solve("doggdog", "dog"))
print(solve("caattcttattacaactaacaaactcaattttcatactcctcttcaactattttaaaccataattattccctacacattcaaacaattccatctacatcacaacttcacttcctaataaaccaatccacatatcatattactctcataccaaataatccaccatattacatccctatttcatcactatactatattaacctcacaatttccattacacaacctaaacttcacttatacccaaaaacctttaccaaccctacactccaacacatactaacaatattacaccacctaccaacataaaatcaactcttccaattaaaaacactctcaaacactccacataacactattacacacctatttaccatcattccacattcacactcaatctcactctctaaaacactaaaatctttcctctcacctctattttcttttattttacttactaccaaaaactaatacacctctctactctaacaaacttctcttacat", "cat"))
print(solve("wwwwwwowwoowowwwwwwowwowowowwwwwwwwoowwwowwowwwowwwwwwwwwwwwwwwwwwwwwwwwwwwwwowooowwowwooowwwoowwoowwowwwwwwwwwwwwwwwowwwwwwooowowwwwwoowwwoooowowowwwwwwwoowowwwwwowwwwwwwowowwooowowoowwowowwwwwowwwwwwwwowwwoowwwwwoowwwoowwwwooowwwwooooooowwoowwoowowwwwwwwwwowwwwwowooowwwwwwwwwowowwwwwwwwowwowwwwwwowwwoowwowwwwwoowwwoowoowwwwwwwowwowowwowwoowwwowwoowwoooowwwowwwwwoowowwwwwwwoowowwwwwooowowooowowwwwowwwooowwwwwowoooowwowowwowowwwowwwwwwwwwowwooowooooooooowoowwoooooowowwwwowooooowwwwwwwwwowwwwwwww", "wow"))