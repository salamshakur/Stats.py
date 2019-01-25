# Statistical functions I've created
import func

# Statistical variables
n      = 0
sum    = 0
mean   = 0
median = 0
mode   = 0
range  = 0
s2     = 0
s      = 0

# Open text file containing values
file  = open("set.txt", "r")

# Insert values into a list
dataSet = func.createList(file)

# Get statistics
n      = len(dataSet)
sum    = func.getSum(dataSet)
mean   = func.getMean(dataSet, sum, n)
median = func.getMedian(dataSet, n)
mode   = func.getMode(dataSet)
range  = func.getRange(dataSet, n)
s2     = func.getSampleVariance(dataSet, mean, n)
s      = func.getStandardDeviation(s2)

# Print statistics
print (dataSet)
print (n)
print (sum)
print (mean)
print (median)
print (mode)
print (range)
print (s2)
print (s)

# Close the file
file.close()
