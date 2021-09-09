# lessons: 
# - graph the matriz as index, it can be helpful
# - Sometimes simply there isn't a visible pattern, and time is gold.
#   so implement the brute force solution and optimice later if exist time
# - Just give some minutes to the task of finding a pattern
def solve(matrix = None):

    # condition of the problem
    if matrix is None: 
        return None

    unique = []
    map = dict()

    len_x = len(matrix[0])
    len_y = len(matrix)
    # left to right
    # all rows
    for i in range(len_y):
        j = 0
        for j in range(len_x):
            target = i-j

            if target in map:
                if map[target] != matrix[i][j]:
                    return -1
            else:
                map[target] = matrix[i][j]
                if matrix[i][j] not in unique:
                    unique.append(matrix[i][j])


    
    return len(unique)

def test():
    test_cases = [
        [[1, 2, 3],
         [3, 1, 2],
         [4, 4, 1],],
        [[1, 2, 3],
         [3, 1, 2],
         [4, 3, 1],],
         None, # no input will be null
        [[1, 2, 3, 4, 8, 1],
         [5, 1, 2, 3, 4, 8],
         [4, 5, 1, 2, 3, 4],
         [7, 4, 5, 1, 2, 3],],
    ]
    expected = [
        -1,
        4,
        None,
        7
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")

test()