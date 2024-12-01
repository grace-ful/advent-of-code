import sys

first_list = []
second_list = []
sum = 0

for line in sys.stdin:
    lineArr = line.split()
    first_list.append(int(lineArr[0]))
    second_list.append(int(lineArr[1]))

first_list.sort()
second_list.sort()

for i in range(0, len(first_list)):
    first = first_list[i]
    second = second_list[i]
    sum += abs(first - second)

print(sum)