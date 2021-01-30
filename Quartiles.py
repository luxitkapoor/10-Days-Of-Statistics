'''The quartiles of an ordered data set are the  points that split the data set into  equal groups. The  quartiles are defined as follows:

: The first quartile is the middle number between the smallest number in a data set and its median.
: The second quartile is the median ( percentile) of the data set.
: The third quartile is the middle number between a data set's median and its largest number.'''


import sys


def floatCheck(number):
    '''
    Added solely to compensate for the fact that Hackerrank's evalutation engine keeps refuting to accept a float output in certain cirumstances. For eg output is 12.0 but their eval engine will only accept 12
    '''
    if number - int(number) == 0:
        return int(number)
    else:
        return number


def calcMedian(size, listOfValues):
    if size % 2 == 0:
        middle = int(size / 2)
        median = (listOfValues[middle] + listOfValues[middle - 1]) / 2

        return floatCheck(median)
    else:
        median = listOfValues[int(size / 2)]
        return floatCheck(median)


data = sys.stdin.readlines()
n = int(data[0].rstrip())
values = [int(i) for i in data[1].rstrip().split()]
middle = int(n / 2)
values.sort()

if n % 2 == 0:
    q2 = (values[middle] + values[middle - 1]) / 2
    q1List = values[:middle]
    q3List = values[middle:]
    q1 = calcMedian(len(q1List), q1List)
    q3 = calcMedian(len(q3List), q3List)

else:
    q2 = values[middle]
    q1List = values[:middle]
    q3List = values[middle + 1:]
    q1 = calcMedian(len(q1List), q1List)
    q3 = calcMedian(len(q3List), q3List)


sys.stdout.write(str(q1) + '\n' + str(floatCheck(q2)) + '\n' + str(q3))
