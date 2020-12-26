# DAY 22
# Part 1

# -------------
# Process input
# -------------
f = open("Day22.txt", "r")

# Initialize our two hands
hand1 = []
hand2 = []

_ = f.readline()
line = f.readline()
while line != '\n':
    # Process hand 1
    line = line.strip('\n')
    hand1.append(int(line))
    line = f.readline()

_ = f.readline()
line = f.readline()
while line:
    # Process hand 1
    # Process hand 1
    line = line.strip('\n')
    hand2.append(int(line))
    line = f.readline()

# Close file
f.close()

# --------------------
# Function Definitions
# --------------------


def play_round():
    """plays a round, comparing top cards and putting both on the bottom of the winner's hand"""

    global hand1, hand2
    # get top cards
    card1 = hand1.pop(0)
    card2 = hand2.pop(0)

    if card1 > card2:  # player 1 won
        # add cards to bottom of hand1
        hand1.append(card1)
        hand1.append(card2)

    else:  # player 2 won
        # add cards to bottom of hand2
        hand2.append(card2)
        hand2.append(card1)

    return

while (len(hand1) > 0 and len(hand2) > 0):
    play_round()

print(hand1, hand2)

# Calculate the score

score = 0
if len(hand1) != 0:  # player 1 won

    for i in range(len(hand1)):
        score += hand1[i] * (len(hand1)-i)
    print('Player 1 won with a score of ', score)

else:  # player 2 won

    for i in range(len(hand2)):
        score += hand2[i] * (len(hand2)-i)
    print('Player 2 won with a score of ', score)