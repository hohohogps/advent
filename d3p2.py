
import re
with open('data3.txt') as file:
    data = file.read().replace('\n', '')
    result = 0
    mul_extracted = re.findall("don't\(\)|do\(\)|mul\(\d+,\d+\)", data)
    enabled = True
    for instr in mul_extracted:
        if instr == "don't()":
            enabled = False
        elif instr == "do()":
            enabled = True
        elif enabled:
            n1, n2 = instr[4:len(instr) - 1].split(",")

            result += int(n1) * int(n2)
    print(result)