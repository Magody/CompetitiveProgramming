

def solve(string):

    len_string = len(string)
    if len_string in [0, 1]:
        return len_string
    
    max_len = 0

    p1 = 0
    p2 = 0
    map = dict()

    while p2 < len_string:
        letter = string[p2]


        if letter in map:
            # already seen
            actual_len = p2 - p1
            # sliding pointer
            if p1 > map[letter]:
                # this is previous data info
                p1 = p2
                # sum 1 for offset
                actual_len += 1
            else:
                # we see in this sequence
                p1 = map[letter] + 1

            if actual_len > max_len:
                max_len = actual_len

        map[letter] = p2
        # add or update found positions
        p2 += 1

    return max_len

def test():

    test_cases = [
        "abcbda",
        "abccabb",
        "cccccc",
        "",
    ]
    expected = [
        4,
        3,
        1,
        0,
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}", error)

test()