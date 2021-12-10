## AOC. DAY 2.
# 
# Read a course from file.
# Commands: forward X, up X, down X.

# Open file with course values
with open('submarine_course_input', 'r') as f:
    # File processing
    course_lines = f.read().splitlines()

# Function negative. Turn integer int a negative integer integer.
def negative(number):
    negative_number = '-' + str(number)
    return int(negative_number)

## DAY 2. PART 1
# Create and initialize a list that updates the coordinates' values, position (F) and depth (D). [F,D]
position = [0,0]
# Additionally, create two lists to save the values of horizontal and depth. The normal should be to save depth readings as negative values (every down command)
# and every up command as a positive value. But I'll do it the other way. Not important, just keep in mind the signs.
horizontal = []
depth = []

# Loop through the course readings, updating position.
# forward X : increase F
# down X : increase D
# up X : decrease D
for el in course_lines:
    if (el.split()[0]) == 'forward':
        position[0] = position[0] + int(el.split()[1])
        horizontal.append(int(el.split()[1]))
    if (el.split()[0]) == 'down':
        position[1] = position[1] + int(el.split()[1])
        depth.append(int(el.split()[1]))
    if (el.split()[0]) == 'up':
        position[1] = position[1] - int(el.split()[1])
        depth.append(negative(el.split()[1]))

print('POSITION: ', position)
#print('Horizontal ', horizontal)
#print('Depth', depth)
print('PART 1. MULTIPLICATION: ', position[0]*position[1])


## DAY 2. PART 2
# New interpretation of commands.
# up X : decrease AIM by X units
# down X : increase AIM by X units
# forward X : increase horizontal AIM by X units
position2 = [0,0]
horizontal2 = []
depth2 = []
aim = 0
aims = [0]

for read in course_lines:
    if (read.split()[0]) == 'up':
        aim = aim - int(read.split()[1])
        aims.append(int(read.split()[1]))
    if (read.split()[0]) == 'down':
        aim = aim + int(read.split()[1])
        aims.append(int(read.split()[1]))
    if (read.split()[0]) == 'forward':
        position2[0] = position2[0] + int(read.split()[1])
        position2[1] = position2[1] + aim * int(read.split()[1])

print('AIM values: ', aims)
print('POSITION 2: ', position2)
print('PART 2. MULTIPLICATION: ', position2[0]*position2[1])
