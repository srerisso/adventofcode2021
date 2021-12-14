## AOC. DAY 3.
# Binary Diagnostic

# power_consumption = gamma_rate * epsilon_rate

# diagnostic_report (input)

# Open file with diagnostic report values
with open('diagnostic_input', 'r') as f:
    # File processing
    diagnostic_lines = f.read().splitlines()

print('Diagnostic values: {}'.format(diagnostic_lines))

bitlist = []
strofbits = ''
count = 0

# Here is the chicha
for element in diagnostic_lines: # Loop through all elements of diagnostic_lines
    for bit in range(0,len(element)-1):  # Loop through all 12 bitlists of every element
        element[bit]
    strofbits = strofbits + element[bit]
    bitlist[count] = strofbits
    count += 1


print(bitlist)