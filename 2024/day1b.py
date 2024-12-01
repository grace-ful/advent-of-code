import sys

first_list = []
second_list = []
sum = 0
mydict = {}

for line in sys.stdin:
    lineArr = line.split()
    first_list.append(int(lineArr[0]))
    second_list.append(int(lineArr[1]))

for i in range(0, len(second_list)):
    value = second_list[i]
    if value in mydict:
        mydict[value] += 1
    else:
        mydict[value] = 1

for i in range (0, len(first_list)):
    value = first_list[i]
    if value in mydict:
        similarity = value * mydict[value]
        sum += similarity

print(sum)