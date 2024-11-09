import math
import traceback
import time
import random
import sys
import copy
sys.setrecursionlimit(10000000)



debug = True

def test():

    test_cases = [
        {"text": "abcdefghi", "sub_text": "de"},
        {"text": "abcdefgci", "sub_text": "c"},
        {"text": "sdkfjslgsd", "sub_text": "magody"},
        {
            "text": "axucgrzqebtbuxpiyuavccltqwcmpzmmfaakncabbbdxepyevkswxhlellrfobyufmyumrorcgmjilzogezuggtxotzukeifvybxkacmwvkhswcoabmgwknminltbdqexopvysobpautmkmiuipuzfqpmwzdprxnadedrquxzassyfgrrjmgfenwmynehqnabgajrnfgdfvftghczetmhcakgnvjuuctufjgoqowhwtozkskaszvfpijugitoextqibynisnfbenweojapwtclszycusagzwbgavxawzfnuhmpddgzyymuxurdqkfkejsqdesmmzlxuokmloduolwyslonilvhjlqtftyxfoaopmvvomiddncnwqmxozqbmhuqpksuydcwwwuxvdfwrfiizcccktmfxcpdtunnknagsgntpnccgimnqketezhsbyrofjvwoqvturvwzttugivywdnqtzjnkyfdzkqcabyinwsoxqlxwecczjgwwcgomuoogaxmbxcwjbjqozjxrzcyojylanjlpcdzgeraxhbaybxsuhcuvlsshmeblbdfaziubugweeckkvxqgtdrrsbxparablqpypqtenytfbntudlyakehtwhbbtngusmjaudcbazjfeqjufbileiwtylkkfkdmtertqzayaohzkuokkuplcwqrcwzxeqlzbhlubycufmwbvvvveeweqmezxxnxmjcajlurjtzuxxjartvvvegmrgpjigfazhpoaqeshxakbcxnghxhddcydmzqgsejyrstktdpcaeqpiqnzyebaioirhvlckxamorbriylesbwszzletemgyfcjyhpsmjandcxdrsjvfzuswuoxybtxzmhjqhbcxbhxdhbxjbrecpuvutlfyamkltfogwklisxhscgvwufckkszpejndjxzsaizjkzuxengwgbpdssryllxmzgejtwmqyehdtymzivyygtqqbcu", 
            "sub_text": "vvve"
        },
        {
            "text": "uepnzleaiogoxbvdcwalayckdzfzxdvddexcofcjlujrzofzolxmigtogtslkwwuxdilwmdjlpaqufnvuuufvhcmwpjqhlchtmqzrijwajbqzwrtzcmbwjvzfdhgunizgddehprykgvbpohccigzyvhintlpwotuvvlzrqicnavvnxfteduomtdjlwqyxbridegazizo", 
            "sub_text": "egazizo"
        },
        {
            "text": "npwaaibtpulwlixduaybxpfqqmshamzfpsbfydhptwdgiblevllgucruzscoewhwhavngcrgyyzbgluhxocbjdcxhysziadikmzebcvbqkvfabfilkqxmksmtflnchewxvosiiumwwpjiegehwosifhqeabccwpblypwgpfrvvaebayysejqekwkshsdvpgjswlanvkd", 
            "sub_text": "npwaaib"
        },

    ]
    expected = [4, 7, -1, 745, 193, 193]
    start = time.process_time()
    for i in range(len(test_cases)):
        solution = None
        try:
            text = test_cases[i]["text"]
            sub_text = test_cases[i]["sub_text"]
            solution = solve(text, sub_text)

            print(solution)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

    end = time.process_time()
    print(f"Elapsed time: {(end - start)*1000}[ms]")


def solve(text, sub_text):
    
    len_text = len(text)
    len_sub_text = len(sub_text)
    p1 = 0
    p2 = len_sub_text - 1

    answer = -1

    while p2 < len_text:
        letter_p1 = text[p1]
        letter_p2 = text[p2]

        if letter_p1 != sub_text[0] and letter_p2 != sub_text[len_sub_text - 1]:
            # p1 += 1
            # p2 += 1
            # p1 = p2 + 1
            # p2 = p2 + len_sub_text
            pass
        elif letter_p1 == sub_text[0] and letter_p2 == sub_text[len_sub_text - 1]:

            found = True
            # intern check
            for i in range(1, len_sub_text-1):

                if text[p1+i] != sub_text[i]:
                    found = False
            
            if found:
                right = len_text - (p1 + len_sub_text)
                left = p1

                maximum = max(right, left)
                if maximum > answer:
                    answer = maximum
        p1 += 1
        p2 += 1
    
    return answer





if debug:
    test()