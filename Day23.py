# DAY 23
# Part 1

# We're starting over because Part 1 was way too slow,
# so I'm going to learn how to build a circular linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return(str(self.data))

class CircleGame:
    def __init__(self, nodes=None):
        self.lookup = {}
        self.head = None
        if nodes is not None:
            node = Node(data=nodes[0])
            self.lookup[node.data] = node
            self.head = node
            for elem in nodes[1:]:
                node.next = Node(data=elem)
                self.lookup[node.data] = node
                node = node.next
            node.next = self.head
            self.lookup[node.data] = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node.next is not self.head:
            nodes.append(str(node.data))
            node = node.next
        nodes.append(str(node.data))
        nodes.append("head")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node.next is not self.head:
            yield node
            node = node.next
        yield node

    def play_game(self, iterations):

        current_cup = self.head
        for i in range(iterations):
            pickups = [current_cup.next.data, current_cup.next.next.data, current_cup.next.next.next.data]
            destination = max_value if current_cup.data == 1 else current_cup.data - 1
            while destination in pickups:
                destination = max_value if destination == 1 else destination - 1

            current_cup.next = current_cup.next.next.next.next
            current_cup = current_cup.next
            self.lookup[pickups[2]].next = self.lookup[destination].next
            self.lookup[destination].next = self.lookup[pickups[0]]


# ----
# Main
# ----

# below is real data
puzzle_input = '186524973'
# below is test data
#puzzle_input = '389125467'

cups = [int(puzzle_input[i]) for i in range(len(puzzle_input))]
max_value = len(cups)
game = CircleGame(cups)
game.play_game(100)

# Get our answer, which is the order of cups after cup 1
node = game.lookup[1]
answer=''
for i in range(max_value - 1):
    answer += str(node.next)
    node = node.next

print("the order after 100 moves is:", answer)

# Part 2

# Now we have to simulate this with 1 million cups and 10 million turns
cups = [int(puzzle_input[i]) for i in range(len(puzzle_input))]
for i in range(10,1_000_001):
    cups.append(i)
max_value = len(cups)
game = CircleGame(cups)
game.play_game(10_000_000)

# Get our answer, which is the product of the two cups after cup 1
node = game.lookup[1]
answer = node.next.data * node.next.next.data

print("the product after 10_000_000 moves is:", answer)
