def f(list):
    dist = 0
    for i in range(len(list)-1):
        temp = int(list[i])-int(list[i+1])
        if (temp == 0) or (abs(temp) not in range (1,4)) or ((dist > 0) and (temp < 0)) or ((dist < 0) and (temp > 0)):
            return False
        dist = temp
    return True

def pop(list):
    j = [list[:i] + list[i+1:] for i in range(len(list))]
    for k in j:
        if f(k) == True:
            return True
    return False
        

safe = 0 
with open('data2.txt') as file:
    data = file.read()
    lines = data.split('\n')
    for line in lines:
        l = line.split()
        if pop(l):
            safe += 1
print(safe)
