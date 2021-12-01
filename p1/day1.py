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

print(len(deepReadings))
print(len(lines))
print(len(deepReadings)-len(lines))


# Second Part of Day 1