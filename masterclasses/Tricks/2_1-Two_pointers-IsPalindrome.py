def isPalindrome(word):
    len_word = len(word)
    p1 = 0
    p2 = len_word-1
    while p1 <= p2:
        if word[p1] != word[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True
