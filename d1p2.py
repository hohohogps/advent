
l_1 = []
l_2 = []
count = 0
with open('data.txt') as file:
    data = file.read()
    lines = data.split('\n')
    for line in lines:
        l = line.split()
        l_1.append(l[0])
        l_2.append(l[1])
l_1.sort()
l_2.sort()
for i in l_1:
    count += int(i)*l_2.count(i)
print(count)