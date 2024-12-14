
l_1 = []
l_2 = []
distance = 0
with open('data.txt') as file:
    data = file.read()
    lines = data.split('\n')
    for line in lines:
        l = line.split()
        l_1.append(l[0])
        l_2.append(l[1])
l_1.sort()
l_2.sort()
for i in range (0,len(l_1)):
    distance += abs(int(l_1[i])-int(l_2[i]))
print(distance)