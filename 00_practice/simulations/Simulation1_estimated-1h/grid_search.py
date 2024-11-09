import math
import traceback
import time
import random
import sys
sys.setrecursionlimit(10000000)



debug = True

def test():

    

    test_cases = [

        {
            "R": 7, "C": 15,
            "G": [
                "111111111111111",  
                "111111111111111",  
                "111111111111111",  
                "111111011111111", 
                "111111111111111",   
                "111111111111111",   
                "101010101010101",  
            ],
            "r": 4, "c": 5,
            "P": [
                "11111",
                "11111",
                "11111",
                "11110",
            ]
        },
        {
            "R": 5, "C": 10,
            "G": [
                "1234567890",  
                "0987654321",  
                "1111111111",  
                "1121223211",
                "2232722222" 
            ],
            "r": 3, "c": 6,
            "P": [
                "1111",
                "2232",
            ]
        },
        {
            "R": 5, "C": 10,
            "G": [
                "1234567890",  
                "0987654331",  
                "1111876543",  
                "8765111111",
                "2222111111",
                "2222111211" 
            ],
            "r": 3, "c": 6,
            "P": [
                "876543",  
                "111111",  
                "111111"
            ]
        },
        {
            "R": 5, "C": 10,
            "G": [
                "1234567890",  
                "0987654331",  
                "1111111211",  
                "1111111111",
                "2222222222" 
            ],
            "r": 3, "c": 6,
            "P": [
                "876543",  
                "111111",  
                "111111"
            ]
        },
        {
            "R": 5, "C": 10,
            "G": [
                "1234567890",  
                "0987654331",  
                "1111111211",  
                "8765431111",
                "2222111111",
                "2222111111" 
            ],
            "r": 3, "c": 6,
            "P": [
                "876543",  
                "111111",  
                "111111"
            ]
        },

    ]
    expected = ["YES", "YES", "YES", "NO", "NO"]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            R = test_cases[i]["R"]
            C = test_cases[i]["C"]
            r = test_cases[i]["r"]
            c = test_cases[i]["c"]
            G = test_cases[i]["G"]
            P = test_cases[i]["P"]
            solution = gridSearch(G, P)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def getPositionOcurrence(string1, pattern, specific_position):

    if specific_position >= 0:
        if string1[specific_position] != pattern[0]:
            return -1
    len_pattern = len(pattern)

    first_index = -1
    i = 0
    index = 0

    while index < len(string1):

        letter = string1[index]


        if letter == pattern[i]:

            if specific_position != -1:
                if index == specific_position:
                    first_index = index
                    i+=1
                elif first_index != -1:
                    i+=1
                    if i == len_pattern:
                        return first_index
            else:
                if first_index == -1:
                    first_index = index
                i+=1
                if i == len_pattern:

                    return first_index
        else:
            if first_index != -1:
                index = first_index + i - 1
                first_index += 1
                if i > 0:
                    i -= 1
            

        index += 1
    # -1 if no match
    return -1


def gridSearch(G, P):
    X = len(G[0])
    Y = len(G)
    M = len(P[0])
    L = len(P)
    i = 0
    while i < Y-(L-1):

        if P[0] in G[i]:

            for b in range(X - (M - 1)):
                j = getPositionOcurrence(G[i], P[0], b)

                if j != -1:
                    # found the first part, so try the rest
                    is_yes = True
                    for p in range(1, L):

                        new_j = getPositionOcurrence(G[i+p], P[p], j)
                        if new_j == -1:
                            is_yes = False
                            break
                    if is_yes:
                        return "YES"
        i += 1




    
    return "NO"

if debug:
    # print(getPositionOcurrence("322273", "2227", -1))
    
    test()

