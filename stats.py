# Statistical variables
list   = []
n      = 0
sum    = 0
mean   = 0
median = 0
mode   = 0
range  = 0

# Open text file containing values
file  = open("set.txt", "r")

# Insert values into set
for line in file:
    x = int(line)
    list.append(x)

# Sort the set
list.sort()

# Get sum of set values
for num in list:
    sum += num

# Get mean
n    = len(list)
mean = sum/n

# Get median
if (n % 2) is not 0:
    i      = (n + 1)/2 - 1
    i      = round(i)
    median = list[i]
else:
    i      = (n + 1)/2 - 1
    left   = int(i)
    right  = round(i)
    median = (list[left] + list[right])/2

# Convert list into a distinct set
set = set(list)

# Create another list to hold frequencies of values original list
freq = []

# Get frequencies of each value in list using the set
for num in set:
    x = list.count(num)
    freq.append(x)

# Find the highest frequency
max = max(freq)

# Convert set back into list for indexing
distinct = []
for num in set:
    distinct.append(num)

# Get mode
if freq.count(max) > 1:
    mode = None
else:
    mode = distinct[max]

# Get range
range = list[n-1] - list[0]

# Sample Variance (S2) - TESTING
x = 0
for num in list:
    x  += (list[num] - mean) * (list[num] - mean)
y = n - 1
s2 = x/y
#

# Close the file
file.close()

print (sum)
print (mean)
print (median)
print (mode)
print (range)
print (s2)
