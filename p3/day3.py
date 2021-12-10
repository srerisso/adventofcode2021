## AOC. DAY 3.
# Binary Diagnostic

# power_consumption = gamma_rate * epsilon_rate

# diagnostic_report (input)

# Open file with diagnostic report values
with open('diagnostic_input', 'r') as f:
    # File processing
    diagnostic_lines = f.read().splitlines()

print('Diagnostic values: {}'.format(diagnostic_lines))

bitlist0 = []
bitlist1 = []
bitlist2 = []
bitlist3 = []
bitlist4 = []
bitlist5 = []
bitlist6 = []
bitlist7 = []
bitlist8 = []
bitlist9 = []
bitlist10 = []
bitlist11 = []

# Here is the chicha
for element in diagnostic_lines: # Loop through all elements of diagnostic_lines
    for bit in range(0,len(element)-1):  # Loop through all 12 bitlists of every element
        #bitlist0[bit].append(element[bit])
        print(bit)

print(bitlist0)
