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

print('The total number of measurements is ') 
print(len(lines))
print('The total number of MAX measurements is ') 
print(len(deepReadings))
print('The total number of measurements larger than the previous is ') 
print(len(lines)-len(deepReadings))

# Second Part of Day 1
# Sum window of 3 elements.
# List of 2000 elements-

intervalReadings = []

0:2
1:3
2:4
3:5    
i,j = 0

for index in (range(lines)):
    intervalReadings.append(lines[i:j])

print(intervalReadings)
