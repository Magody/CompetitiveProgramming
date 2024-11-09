def solve():
    n = int(input())
    
    numbers = []
    for i in range(n):
        numbers.append(input())
    
    numbers_length = len(numbers)
    number_length = len(numbers[0])

    code = 0
    for i in range(number_length):
        first_number = numbers[0][i]
        for j in range(numbers_length):
            if numbers[j][i] != first_number:
                print(code)
                return

        code = code + 1
    
    print(code)

solve()
