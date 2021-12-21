## #################################
## AOC. DAY 3. PART 2.
#  Calculate Life Support Rating
#
# life support rating = O2 generator rating * CO2 scrubber rating
#
# INPUT: diagnostic_report
#
# Open file with diagnostic report values


def findO2rating(str1):
    return "O2 rating finder"


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

print('Diagnostic values: {}'.format(diagnostic_lines))