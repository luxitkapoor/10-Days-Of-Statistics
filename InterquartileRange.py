import sys


def calcMedian(size, listOfValues):
    if size % 2 == 0:
        middle = int(size / 2)
        median = (listOfValues[middle] + listOfValues[middle - 1]) / 2

        return median
    else:
        median = listOfValues[int(size / 2)]
        return median


inputData = sys.stdin.readlines()
n = int(inputData[0].rstrip())
x = [int(i) for i in inputData[1].rstrip().split()]
f = [int(i) for i in inputData[2].rstrip().split()]
s = []
for index, value in enumerate(x):
    s += [value] * f[index]

middle = int(len(s) / 2)
s.sort()
if middle % 2 == 0:
    q1List = s[:middle]
    q3List = s[middle:]
    q1 = calcMedian(len(q1List), q1List)
    q3 = calcMedian(len(q3List), q3List)
else:
    q1List = s[:middle]
    q3List = s[middle + 1:]
    q1 = calcMedian(len(q1List), q1List)
    q3 = calcMedian(len(q3List), q3List)

iqr = q3 - q1
sys.stdout.write(str(float(iqr)))
