import math
import traceback

debug = True

def test():

    test_cases = [
        { "k": 10, "j": 10},
        { "k": 6, "j": 7},
        { "k": 5, "j": 4},
        { "k": 4, "j": 5},
        { "k": 9, "j": 3},
        { "k": 4, "j": 3},
        { "k": 2, "j": 1},
        { "k": 1000000, "j": 10000000000},
        { "k": 0, "j": 10000000000},
        { "k": 0, "j": 0},
        { "k": 3, "j": 2},
        { "k": 2, "j": 4},
        { "k": 2, "j": 5},
        { "k": 4, "j": 3},
        { "k": 3, "j": 5},
        { "k": 4, "j": 4},
        { "k": 527, "j": 300},
        { "k": 300, "j": 300},

    ]
    expected = [
        6,
        4,
        3,
        3,
        3,
        2,
        1,
        1000000,
        0,
        0,
        1,
        2,
        2,
        2,
        2,
        2,
        275,
        200,
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            k = test_cases[i]["k"]
            j = test_cases[i]["j"]
            solution = solve(k, j)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())


def is_valid_pair(k, j):
    return (k > 0 and j > 0) and not (k == 1 and j == 1)

def solve(k, j):
    answer = 0
    lower = k
    higher = j
    if j < k:
        lower = j
        higher = k
    
    while is_valid_pair(lower, higher):

        if lower == 1 or higher == 1:
            answer += 1
            break
        

        # step
        higher_possible_pairs = max(math.floor(higher/4), 1)
        if lower < higher_possible_pairs:
            higher_possible_pairs = lower

        higher = higher - (higher_possible_pairs * 2)
        lower -= higher_possible_pairs

        answer += higher_possible_pairs

        if higher < lower:
            temp = lower
            lower = higher
            higher = temp
    
    
    return answer

if debug:
    test()
else:
    k, j = map(int, input().split(" "))
    print(solve(k, j))

