import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦️', '♣️', '♠️']

deck = [rank + suit for rank in ranks for suit in suits]
random.shuffle(deck)

player_hand = deck[:5]
computer_hand = deck[:5]

player_score = 0
computer_score = 0
for i in range(5):
    if ranks.index(player_hand[i][0]) > ranks.index(computer_hand[i][0]):
        player_score += 1
    elif ranks.index(player_hand[i][0]) < ranks.index(computer_hand[i][0]):
        computer_score += 1

print("Player's hand:", player_hand)
print("Computer's hand:", computer_hand)
if player_score > computer_score:
    print("Player wins!")
elif player_score < computer_score:
    print("Computer wins!")
else:
    print("It's a tie!")
