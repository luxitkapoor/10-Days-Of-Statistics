import sys
from math import sqrt

inputData = sys.stdin.readlines()
n = int(inputData[0].rstrip())
x = [int(i) for i in inputData[1].rstrip().split()]

mean = sum(x) / n

distanceSquared = 0
for i in x:
    distanceSquared += (i - mean) ** 2

variance = distanceSquared / n
standardDeviation = sqrt(variance)

sys.stdout.write(str(round(standardDeviation, 1)) + '\n')
