# Open text file containing values
file = open("set.txt", "r")

# Create list
list = []

# Insert values into set
for line in file:
    x = int(line)
    list.append(x)

# Sort the set
list.sort()

# Get sum of set values
sum = 0
for num in list:
    sum+=num

# Get mean
n    = len(list)
mean = sum/n

# Get median
left   = 0
right  = 0
median = 0

if (n % 2) is not 0:
    i = (n + 1)/2 - 1
    i = round(i)
    median = list[i]
else:
    i = (n + 1)/2 - 1
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
mode = 0
if freq.count(max) > 1:
    mode = 0
else:
    mode = distinct[max]
