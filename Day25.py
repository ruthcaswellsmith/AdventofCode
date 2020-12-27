# DAY 25
# Part 1

def handshake(subject_number, loop_size):
    '''calculates a handshake based on subject_number and loop_size'''
    value = 1
    for loop in range(loop_size):
        value *= subject_number
        value = value%20201227

    return value

def find_loop_size(subject_number, key):
    """tries different loop size until a match is found"""

    value = 1
    loop_size = 1
    while True:
        value *= subject_number
        value = value%20201227
        if value == key:
            return loop_size
        loop_size += 1

# set keys
card_public_key = 6930903
door_public_key = 19716708
# card_public_key = 5764801
# door_public_key = 17807724

#print(handshake(7, 8))
#print(handshake(7, 11))

# Find the loop size
card_loop_size= find_loop_size(7, card_public_key)
door_loop_size= find_loop_size(7, door_public_key)

print(card_loop_size, door_loop_size)
# Now calculate the encryption key
print(handshake(door_public_key,card_loop_size))
print(handshake(card_public_key,door_loop_size))
