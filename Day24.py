# DAY 24
# Part 1

# import packages
import numpy as np

#----------
# Functions
#----------
def process_direction(direction):
    """processes a string of directions, flipping the resulting tile"""
    print('processing direction:', direction)
    i, j = ref_i, ref_j

    while len(direction) > 0:
        # get next tile
        if direction[0:2] in ['se', 'sw', 'ne', 'nw']:
            next_tile = direction[0:2]
            direction = direction[2:]
        else:
            next_tile = direction[0:1]
            direction = direction[1:]

        # move to next tile
        i, j = i + offsets[next_tile]['i'], j + offsets[next_tile]['j']

    # flip tile
    floor[i][j] = 0 if floor[i][j] else 1

    return

# Initialize our floor
num_dim = 1000
floor = np.zeros([num_dim, num_dim], dtype='bool')

# Pick our center tile
ref_i = 500
ref_j = 500

# Initialize our dictionary of offsets
offsets =   {'ne': {'i': -1, 'j': +1},
             'nw': {'i': -1, 'j': -1},
             'se': {'i': +1, 'j': +1},
             'sw': {'i': +1, 'j': -1},
             'e':  {'i':  0, 'j': +2},
             'w':  {'i':  0, 'j': -2}}

# ----------------------
# Read and process input
# ----------------------

# Open file
f = open("Day24.txt", "r")

line = f.readline()
while line:

    # Process the line
    line = line.strip('\n')
    if line != '':
        process_direction(line)

    line = f.readline()

# Close file
f.close()

black_tiles = np.sum(np.sum(floor))
print("number of black tiles is", black_tiles)

# Part 2

#----------
# Functions
#----------

def count_neighbors():
    """creates an array which contains the number of neighboring black tiles for each tile"""

    neighbors = np.zeros([num_dim, num_dim], dtype='int')

    i_array, j_array = np.where(floor)
    for ind in range(len(i_array)):
        for offset in offsets.keys():
            i_neighbor, j_neighbor = i_array[ind] + offsets[offset]['i'], j_array[ind] + offsets[offset]['j']
            neighbors[i_neighbor][j_neighbor] += 1

    return neighbors

# ----
# Main
# ----

for day in range(1,101):

    print('counting neighbors')
    neighbors = count_neighbors()
    print('finished neighbors')

    # This will result in a matrix with 1's for black tiles that have 0 or more than 2 black neighbors
    flip_black = np.logical_and(floor, np.logical_or(neighbors>2, neighbors==0))

    # This will result in a matrix with 1's for white tiles that have 2 black neighbors
    flip_white = np.logical_and( floor==False, neighbors==2)

    # Now put these together
    flip = np.logical_or(flip_black, flip_white)

    # Now we flip the floor tiles with a logical xor
    floor = np.logical_xor(floor, flip)

    print('after day', day, ': ', np.sum(np.sum(floor)))