from typing import List

# lessons:
# - Learn the data structures already integrated in
#   the programming language. In python a list can be
#   stack, queue and linked list simple (no circular)

def solve(string):
    if string == "":
        return True

    # stack = FILO = First input, Last output
    stack = []

    map = {
        "}": "{",
        "]": "[",
        ")": "(",
        "{": True,
        "[": True,
        "(": True
    }

    for i in range(len(string)):
        # will detect only right part
        value = string[i]
        if map[value] == True:
            stack.append(value)
        else:
            # is oposite
            if len(stack) == 0:
                return False
            else:
                popped = stack.pop() # FILO
                if map[value] != popped:
                    return False

    
    
    return len(stack) == 0

def test():
    test_cases = [
        "{([])}",
        "{([]",
        "{[(])}",
        "{[]()}",
        "",
    ]
    expected = [
        True,
        False,
        False,
        True,
        True,
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