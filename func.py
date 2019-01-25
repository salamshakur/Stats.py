def createList(file):
    list = []
    for line in file:
        x = int(line)
        list.append(x)
    list.sort()
    return list

def getSum(list):
    sum        = 0
    for num in list:
        sum    = sum + num
    return sum;

def getMean(list, sum, n):
    mean       = sum/n
    return mean;

def getMedian(list, n):
    median     = 0
    if (n % 2) is not 0:
        i      = (n + 1)/2 - 1
        i      = round(i)
        median = list[i]
    else:
        i      = (n + 1)/2 - 1
        left   = int(i)
        right  = round(i)
        median = (list[left] + list[right])/2
    return median;

def getMode(list):
    sets       = set(list)
    freq       = []
    mode       = 0
    for num in sets:
        x      = list.count(num)
        freq.append(x)
    most       = max(freq)
    distinct   = []
    for num in sets:
        distinct.append(num)
    if freq.count(most) > 1:
        mode   = None
    else:
        mode   = distinct[most]
    return mode;

def getRange(list, n):
    range      = list[n-1] - list[0]
    return range;
