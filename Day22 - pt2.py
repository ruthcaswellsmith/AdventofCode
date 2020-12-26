# DAY 22
# Part 2

# -------------
# Process input
# -------------
f = open("Day22.txt", "r")

# Initialize our two hands
hand_1 = []
hand_2 = []

_ = f.readline()
line = f.readline()
while line != '\n':
    # Process hand 1
    line = line.strip('\n')
    hand_1.append(int(line))
    line = f.readline()

_ = f.readline()
line = f.readline()
while line:
    # Process hand 1
    # Process hand 1
    line = line.strip('\n')
    hand_2.append(int(line))
    line = f.readline()

# Close file
f.close()

# -------------------
# Function Definition
# -------------------


def play_combat(hand1, hand2):
    """this function plays recursive combat given two arrays hands cards,
    returning the winner of the game and their hands for scoring"""

    round = 0
    stored_hands_1 = set()
    stored_hands_2 = set()

    # play until either hand is empty
    while (len(hand1) > 0 and len(hand2) > 0):

        round += 1
        # before playing a round, check previous hands
        # if we've had them before the winner is player1
        if (tuple(hand1) in stored_hands_1) and (tuple(hand2) in stored_hands_2):
            return 'player1', hand1, hand2

        # save these hands
        if tuple(hand1) not in stored_hands_1:
            stored_hands_1.add(tuple(hand1))
        if tuple(hand2) not in stored_hands_2:
            stored_hands_2.add(tuple(hand2))

        # otherwise draw cards
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)

        if len(hand1)>=card1 and len(hand2)>=card2:
            # both players have enough cards so they play a sub-game
            # we don't need to do anything with the hands returned
            # if player1's highest card beats player2's highest card then player1 will always win
            if max(hand1) > max(hand2):
                winner = 'player1'
            else:
                winner, h1, h2 = play_combat(hand1[0:card1].copy(), hand2[0:card2].copy())

        else:
            # we just compare card1 and card2
            if card1 > card2:  # player1 won
                winner = 'player1'
            else:  # player2 won
                winner = 'player2'

        if winner == 'player1':
            hand1.append(card1)
            hand1.append(card2)
        else:  # player2 won
            hand2.append(card2)
            hand2.append(card1)

    # if we're here, then one of the players is out of cards
    #print('someone is out of cards')
    if len(hand1) != 0:  # player1 won
        return 'player1', hand1, hand2

    else:  #player2 won
        return 'player2', hand1, hand2


# ----
# Main
# ----

winner, hand_1, hand_2 = play_combat(hand_1, hand_2)
print(winner)
print(hand_1)
print(hand_2)

# Calculate the score
if len(hand_1) != 0:  # player 1 won
    score = sum(((i + 1) * v for i, v in enumerate(reversed(hand_1))))
    print('Player 1 won with a score of ', score)

else:  # player 2 won
    score = sum(((i + 1) * v for i, v in enumerate(reversed(hand_2))))
    print('Player 2 won with a score of ', score)