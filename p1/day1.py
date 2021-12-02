### ADVENT OF CODE 2021. DAY 1 ### 

# Load and Analyze input finding increased measurements
# 1. load ipnut file in a data structure

# 2. analyze input values. Find MAX
# 
# readv = file.read
# if readv > lastv
#    lastv = readv
#    readv = file.read
# else 
#   max = lastv
#import numpy as np


with open('input', 'r') as f:
    # File processing goes here
    lines = f.read().splitlines()
    deepReadings = []    
    max = ''
#    print(lines)

    for el in lines:
        if el >= max:
            max = el
        else:
            deepReadings.append(max)
            max = el

print("The total number of measurements is ") 
print(len(lines))
print('The total number of MAX measurements is ') 
print(len(deepReadings))
print('The total number of measurements larger than the previous is ') 
print(len(lines)-len(deepReadings))

### DAY 1. Second Part. ###
# Sum window of 3 elements.
# List of 2000 elements

intervalReadings = []
i = 0
j = 3
window = 3

newlen = len(lines)
print(newlen)
newlen = newlen - (len(lines) % window)
print(newlen)

for elem in range(0,newlen):
    intervalReadings.append(lines[i:j])
    i = i+1
    j = j+1

# We have created intervalReadings, a list of sublists of lines. Each sublist has 3 (window) elements
# Now, we need the sum of each 3 elements.
print(intervalReadings)
