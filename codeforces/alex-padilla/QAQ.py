def solve():
    test_case = input()

    count = 0

    i = 0
    j = len(test_case) - 1
    left_qs = 0
    right_qs = 0

    memo = {}

    while j >= 0 :
        if test_case[i] == "Q":
            left_qs = left_qs + 1

        if test_case[i] == "A":
            if i not in memo:
                memo[i] = {}
            memo[i]["left_qs"] = left_qs

        if test_case[j] == "Q":
            right_qs = right_qs + 1

        if test_case[j] == "A":
            if j not in memo:
                memo[j] = {}
            memo[j]["right_qs"] = right_qs

        i = i + 1
        j = j - 1

    for i in memo:
        if memo[i]["left_qs"] != 0 and memo[i]["right_qs"] != 0:
            count = count + max(memo[i]["left_qs"], memo[i]["right_qs"])

    print(count)

solve()
