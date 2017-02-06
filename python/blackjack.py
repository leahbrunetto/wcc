import random
print('Welcome to Blackjack!')
print

# Setup
# Initialize the deck and shuffle it

#                                       J   Q   K
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
random.shuffle(cards)

# Round 1
# The computer and player are each dealt one card each. Display each player's hand after they receive them.

player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

#print(cards) # To see the list after two cards have been popped off.

# Round 2
# The computer always hits in this round. Pop off one card from the cards list and add it to the computer's hand.
# The user is asked if they want to stay or hit. If the user hits, pop off one card from the cards list and add it to the user's hand. If they stay, don't do anything (i.e. set their second "card" to 0).
# Print the computer's updated set of cards
# Print the user's updated set of cards

computer_card2 = cards.pop()

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if (decision == 'h'):
    player_card2 = cards.pop()
if (decision == 's'):
    player_card2 = 0
    
print('Your cards: ' + str(player_card1) + ', ' + str(player_card2))
print('Computer cards: ' + str(computer_card1) + ', ' + str(computer_card2))

# Round 3
# The computer hits if the sum of the cards is less than 16. Make sure to convert string values to integer!
# The user is asked if they want to stay or hit. If the user hits, pop off one card from the cards list and add it to the user's hand. If they stay, don't do anything.
# Print the computer's updated set of cards
# Print the user's updated set of cards

if (computer_card1 + computer_card2 < 16):
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if (decision == 'h'):
    player_card3 = cards.pop()
else:
    player_card3 = 0

print('Your cards: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
print('Computer cards: ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))

# Game Conclusion
# Add up the total of the cards for both the computer and the user. If both players scored over 21, print "Tie". If both players have the same score, print "Tie". If the computer only scored over 21, print "You won!". If only player scored over 21, print "You lost!". If player's total was more than the computer's total, print "You lost!". If computer's total was more than the player's total, print "You won!"

print('Game over')
player_total = player_card1 + player_card2 + player_card3
computer_total = computer_card1 + computer_card2 + computer_card3

if (player_total > 21 and computer_total > 21):
    print('Tie!')
elif (player_total == computer_total):
    print('Tie!')
elif (computer_total > 21):
    print('You won!')
elif (player_total > 21):
    print('You lost!')
elif (player_total > computer_total):
    print('You lost!')
else:
    print('You won!')

