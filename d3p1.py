import re

pattern = r"mul\(\d+,\d+\)"


with open('data3.txt') as file:
    data = file.read().replace('\n', '')

    matches = re.findall(pattern, data)


    n = 0
    
    for i in matches:
        j = str(i[4:-1])
        k = j.split(',')
        n += int(k[0])*int(k[1])

    print(n)