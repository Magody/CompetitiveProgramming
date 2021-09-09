import math

def get_not_adj(index, array):
    new_array = []
    for i, element in enumerate(array):
        # i < index - 1 or 
        if element != math.inf and (i > index + 1) and not (index == 0 and i == len(array) - 1):
            new_array.append(element)
        else:
            new_array.append(math.inf)
        
    return new_array

def get_elements(no_adj):

    elements = []
    for element in no_adj:
        if element != math.inf:
            elements.append(element)

    return elements

def tree(actual, original, elements, value, level, memo = dict()):

    if len(elements) == 0:
        return actual

    key = ""
    for data in original:
        if data == math.inf:
            key += "-"
        else:
            key += str(data)

    if key in memo:
        return actual + memo[key]

    sums = []
    # elements is correct
    for i, element in enumerate(elements):

        the_index = -1
        for j in range(len(original)):
            if original[j] == element:
                the_index = j
                break

        """if the_index in memo:
            answer = memo[the_index]
        else:"""
        no_adj = get_not_adj(the_index, original)
        new_elements = get_elements(no_adj)

        answer = tree(element, no_adj, new_elements, 0, level+1)
        
        memo[the_index] = answer

        if answer is not None:
            sums.append(answer)

    memo[key] = max(sums)
        
    return actual + memo[key]



def solve(rooms):
    len_rooms = len(rooms)

    answer = tree(0, rooms, rooms, 0, 0)

            





    
    
    return answer


print(solve([1,2]))
print(solve([2,1,3]))
print(solve([1,2,7,4,2]))
print(solve([94,65,50,17,17,14,37,61,67,29,10,99,9,21,7,90,53,51,9,11,53,90,68,24,57,72,79,44,26,50,100,44,78,14,75,62,12,27,34,90,11,40,57,89,21,57,24,48,93,0,18,99,92,28,38,81,85,0,23,14,54,10,16,60,99,14,57,67,13,85,81,37,76,40,21,41,63,40,64,90,28,47,83,46,27,8,79,13,88,61,17,7,82,45,43,98,27,48,18,10]))
print(solve([78,11,69,38,77,78,6,11,80,95,10,18,39,2,46,5,75,80,65,40,5,93,22,16,31,99,45,38,72,71,57,36,26,78,47,52,6,7,97,57,24,79,5,94,79,97,23,44,66,43,37,68,18,20,96,49,49,69,28,92,34,21,97,75,11,49,22,81,80,14,61,59,55,73,26,73,93,72,95,81,71,99,76,11,83,71,91,18,40,15,27,99,61,29,88,50,81,57,36,81]))