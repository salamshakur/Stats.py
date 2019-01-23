# Open text file containing values
file = open("set.txt", "r")

# Create set
set = []

# Insert values into set
for line in file:
    x = int(line)
    set.append(x)

# Sort the set
set.sort()

# Get sum of set values
sum = 0
for num in set:
    sum+=num

# Get mean
n    = len(set)
mean = sum/n

# Get median
left   = 0
right  = 0
median = 0

if (n % 2) is not 0:
    i = (n + 1)/2 - 1
    i = round(i)
    median = set[i]
else:
    i = (n + 1)/2 - 1
    left   = int(i)
    right  = round(i)
    median = (set[left] + set[right])/2
