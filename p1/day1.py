### ADVENT OF CODE 2021. DAY 1 ### 

## Functions created for these DAY 1.

# find_increases
# Given a list of unordered readings from a sonar, find how many times 
# there's a max depth reading.
def find_increases(list):
    deepReadings = []
    incDeeps = []
    max = 0
    counter = 0

    for el in list:
        if (el > max) and (max != 0):
            incDeeps.append(el)
            max = el
        else:
            deepReadings.append(el)
            counter = counter+1
            max = el

    print("The total number measurements is ", len(list)) 
<<<<<<< HEAD
    print('Total deep Readings ', len(deepReadings)) 
    print('Total inc Deeps ', len(incDeeps)) 
=======
    print('Total decreasing measurements ', len(deepReadings)) 
    print('Total increasing measurements ', len(incDeeps)) 
>>>>>>> 3eb5fd38b1d1de887de4cdedc0530f8b5c755c17
    print('The total number of measurements larger than the previous is ') 
    print(len(list)-len(deepReadings))
#    print('Counter: ', counter)

#    return(len(lines)-len(deepReadings))
    return(incDeeps)

# suml 
# Return the sum of all the elements in a list
def suml(list):
    sum = 0
    for el in list:
        sum = sum + int(el)
    return sum

## PART 1 ##
# Load and Analyze input finding increased measurements
# 1. load input file in a data structure (a list).

# 2. analyze input values. Find MAX depth values.

## Open file with input values
with open('input', 'r') as f:
    # File processing
    lines = f.read().splitlines()

integer_lines = map(int, lines)
intlines_list = list(integer_lines)
intlines_list.pop(0) # Eliminate the first element for this case.
#print("Total number of MAX depth readings: ", len(lines)-len(find_increases(intlines_list)))
print(find_increases(intlines_list))

## PART 2 ##
# Sum window of n elements (window)
# List of n elements (lines)

intervalReadings = []
i = 0
j = 3
window = 3

newlen = len(lines)
#print("New length: ", newlen)
#newlen = newlen - (len(lines) % window)
#print("New Length updated: ", newlen)

for elem in range(0,newlen):
    if j == (newlen+1):
        break
    else:
        intervalReadings.append(lines[i:j])
        i = i+1
        j = j+1

# We have created intervalReadings, a list of sublists of lines. Each sublist has 3 (window) elements
# Now, we need the sum of each 3 elements.

intervalSumReadings = []

intervalSumReadings = map(suml, intervalReadings)
listSumReadings = list(intervalSumReadings)
listSumReadings.pop(0)
#print('ListSumReadings', listSumReadings)
print('*** ******************************** ***')
#print(len(intlines_list)-len(find_increases(list(intervalSumReadings))))
#print("Total number of MAX depth readings (Window system): ", find_increases(list(intervalSumReadings)))
print(find_increases(listSumReadings))

# Answer is NOT: 1732