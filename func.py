def createList(file):
    list        = []
    for line in file:
        x       = int(line)
        list.append(x)
    list.sort()
    return list

def getSum(list):
    sum         = 0
    for num in list:
        sum     = sum + num
    return sum;

def getMean(list, sum, n):
    mean        = sum/n
    return round(mean, 3);

def getMedian(list, n):
    median      = 0
    if (n % 2) is not 0:
        i       = (n + 1)/2 - 1
        i       = round(i)
        median  = list[i]
    else:
        i       = (n + 1)/2 - 1
        left    = int(i)
        right   = round(i)
        median  = (list[left] + list[right])/2
    return median;

def getMode(list):
    sets        = set(list)
    freq        = []
    mode        = 0
    count       = 0
    tracker     = 0
    for num in sets:
        if list.count(num) > count:
            count = list.count(num)
            tracker = num
        freq.append(list.count(num))
    most = max(freq)
    if freq.count(most) > 1:
        mode    = None
    else:
        mode    = tracker
    return mode;

def getRange(list, n):
    range       = list[n-1] - list[0]
    return range;

def getSampleVariance(list, mean, n):
    temp        = []
    for num in list:
        x       = (num - mean) ** (2.0)
        temp.append(x)
    numerator   = getSum(temp)
    denominator = n - 1
    return round((numerator/denominator), 3);

def getStandardDeviation(s2):
    s           = s2 ** (.5)
    return round(s, 3);

def getCoefficientOfVariation(s, mean):
    return round(((s/mean) * 100), 3);

def getZScore(list, mean, s):
    zScores     = []
    for num in list:
        x       = (num-mean)/s
        zScores.append(round(x, 3))
    return zScores;
