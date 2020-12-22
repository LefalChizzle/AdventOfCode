from collections import deque
with open('files/day22.txt') as file:
    inp = file.read().split("\n\n")
    deck_one = [int(i) for i in inp[0].split(":\n")[1].split()]
    deck_two = [int(i) for i in inp[1].split(":\n")[1].split()]
# print(deck_one)
# print(deck_two)
while len(deck_two) > 0 and len(deck_one) > 0:
    # print(deck_one)
    # print(deck_two)
    x = deck_one.pop(0)
    y = deck_two.pop(0)
    if x > y:
        deck_one.extend([x])
        deck_one.extend([y])
    elif x < y:
        deck_two.extend([y])
        deck_two.extend([x])
    # print(x)
    # print(y)
# print(deck_one)
# print(deck_two)
winner1 = deck_one if len(deck_one) > 0 else deck_two
ans1 = sum([(len(winner1) - i) * winner1[i] for i in range(len(winner1))])
print(f"part1: {ans1}")
deck_one = [int(i) for i in inp[0].split(":\n")[1].split()]
deck_two = [int(i) for i in inp[1].split(":\n")[1].split()]


def recursive_play(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        # Checking to see if instant win occurs
        # this is defintely balanced
        current_state = (tuple(deck1), tuple(deck2))
        # list are unhashable apparently
        if current_state in seen:
            return 1, deck1
        seen.add(current_state)
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            sub1 = list(deck1)[0:card1]
            sub2 = list(deck2)[0:card2]
            winner = recursive_play(list(sub1), list(sub2))[0]
        else:
            winner = 1 if card1 > card2 else 2
        if winner == 1:
            deck1.extend([card1])
            deck1.extend([card2])
        else:
            deck2.extend([card2])
            deck2.extend([card1])
    return (1, deck1) if deck1 else (2, deck2)


winner2 = recursive_play(deck_one, deck_two)[1]
ans2 = sum([(len(winner2) - i) * winner2[i] for i in range(len(winner2))])
print(f"part2: {ans2}")
