## #################################
## AOC. DAY 3. PART 2.
#  Calculate Life Support Rating
#
# power_consumption = gamma_rate * epsilon_rate
#
# diagnostic_report (input)
#
# Open file with diagnostic report values

from typing import Counter

## Function findGamma
# Find the most common bit
def findGamma(str1):
    gammaRate = ''
    c=Counter(str1)
    if c['0'] > c['1']:
        gammaRate = '0'
    else:
        gammaRate = '1'

    # print('Gamma rate: {}'.format(gammaRate))
    return gammaRate    

## Function findEpsilon
# Find the least common bit
def findEpsilon(str1):
    epsilonRate = ''
    c=Counter(str1)
    if c['0'] > c['1']:
        epsilonRate = '1'
    else:
        epsilonRate = '0'
        
    # print('Epsilon rate: {}'.format(epsilonRate))
    return epsilonRate 


## #################################
# Here is the main process.
# for element in diagnostic_lines: # Loop through all elements of diagnostic_lines

# Define a Dictionary to hold all values of every bit position
#
# dictBits = [(0:'110001100 ... 0011'), (1:'010101100 ... 0101'), ... , (11:'000001100 ... 0111')

# Open file and read input values.
with open('diagnostic_input', 'r') as f:
    # File processing
    diagnostic_lines = f.read().splitlines()

# print('Diagnostic values: {}'.format(diagnostic_lines))

dictBits = {}
count = -1

for el in diagnostic_lines:
    # bitlist=[]
    count = count+1
    for bit in range(0,12):
        # dictBits[bit] = el[bit]
        # update dict value with previous value
        if count == 0: # first iteration, there's nothing in the dictionary
            dictBits[bit] = el[11-bit]
        else:
            dictBits[bit] = dictBits[bit] + el[11-bit]

# print(dictBits)
print(dictBits.values())
#
# dictBits.values = ()

epsilonR = ''
gammaR = ''

for element in reversed(dictBits.values()):
    c=findGamma(str(element))
    gammaR = gammaR + c
    d=findEpsilon(str(element))
    epsilonR = epsilonR + d

print('Gamma Rate is: {}'.format(gammaR))
print('Epsilon Rate is: ', epsilonR)
print('Power Consumption is: ', gammaR * epsilonR)