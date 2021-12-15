## AOC. DAY 3.
# Binary Diagnostic

# power_consumption = gamma_rate * epsilon_rate

# diagnostic_report (input)

# Open file with diagnostic report values
from typing import Counter


with open('diagnostic_input', 'r') as f:
    # File processing
    diagnostic_lines = f.read().splitlines()

# print('Diagnostic values: {}'.format(diagnostic_lines))

# checkListValues : given a list of binary values, find the most common value for every bit position.

# def findMax(list):
    # loop through list


# Here is the main process.
# for element in diagnostic_lines: # Loop through all elements of diagnostic_lines

# Define a Dictionary to hold all values of every bit position
#
# dictBits = [(0:'110001100 ... 0011'), (1:'010101100 ... 0101'), ... , (11:'000001100 ... 0111')

dictBits = {}
count = -1

for el in diagnostic_lines:
    # bitlist=[]
    count = count+1
    for bit in range(0,12):
        # dictBits[bit] = el[bit]
        # update dict value with previous value
        if count == 0: # first iteration, there's nothing in the dictionary
            dictBits[bit] = el[bit]
        else:
            dictBits[bit] = dictBits[bit] + el[bit]

print(Counter(dictBits[0]))
