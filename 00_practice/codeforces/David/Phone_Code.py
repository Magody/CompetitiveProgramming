#https://codeforces.com/problemset/problem/172/A
def myFunction():
    num = int(input())
    phoneNumbers = []
    for i in range(num):
        phoneNumbers.append(input())
    
    longestCommon = 0

    for i in range(len(phoneNumbers[0])):
        curNumber = phoneNumbers[0][i]
        flag = True
        for j in range(1, num):
            if phoneNumbers[j][i] != curNumber:
                flag = False
                break
        if flag:
            longestCommon += 1
        else:
            break      
    print(longestCommon)

myFunction()
