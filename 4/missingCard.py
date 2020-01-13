# There was a set of cards with numbers from 1 to N.
#  One of the card is now lost. Determine the number 
#  on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - 
# representing the numbers on the remaining cards 
# (distinct integers in the range from 1 to N). 
# Find and print the number on the lost card.

n = int(input())

#creating an empty deck
deck = [False for num in range(n+1)]

# filling up the deck
for num in range(n+1):
    card = int(input())
    deck[card+1] = True
    
for card in deck:
    if deck[card] == False:
        print(card+1)