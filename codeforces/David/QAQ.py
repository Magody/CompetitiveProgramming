#https://codeforces.com/problemset/problem/894/A

def myFunction(text:str):
    filteredText = ""
    cont = 0
    for char in text:
        if char in "QA":
            filteredText += char
    
    #brute force
    for i in range(len(filteredText)-2): #Q
        if filteredText[i] == "Q":
            for j in range(i+1, len(filteredText)-1): #A
                if filteredText[j] == "A":
                    for k in range(j+1, len(filteredText)): #Q
                        if filteredText[k] == "Q":
                            cont += 1
    print(cont)

#test
values = [
    "QAQAQYSYIOIWIN",
    "QAQQQZZYNOIWIN"
]    

for val in values:
    myFunction(val)                    