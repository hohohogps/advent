from itertools import product
combinations = {}

def test(prod, key, value):

    ans = value[0]
    for i in range (1,len(value)):
        if prod[i-1] == '+':
            ans += value[i]
        elif prod[i-1] == '*':
            ans *= value[i]
        elif prod[i-1] == '|':
            ans = str(ans)
            ans += str(value[i])
            ans = int(ans)
        
    return ans == key

result = 0

with open ('data7.txt') as file:
    data = file.read()
    lines = data.split('\n')

    for line in lines:
        line_pair = line.split(': ')
        key = int(line_pair[0])
        value = list(map(int,line_pair[1].split()))

        for prod in product('*+|', repeat = len(value)-1):
            if test(prod, key, value):
                result += key
                break

print(result)


