############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from replit import clear
import random
from art import logo



# Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over 21, you lose!"
  
  if user_score == 0:
    return "You have a blackjack, you win!"
  elif computer_score == 0:
    return "The dealer has a blackjack, you lose!"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "The dealer went over. You win" 
  elif user_score == computer_score:
    return "It is a draw"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def blackjack():
  
  print(logo)

  user_cards = []
  computer_cards = []
  play_game = True

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while play_game:
    user_score =calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your starting deck is {user_cards} and your current score is {user_score}")
    print(f"The computer first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
     play_game = False

    else:
      choice = input("Do you want to hit or stand? H for hit S for stand\n").lower()
      if choice == 'h':
        user_cards.append(deal_card())
      else:
        play_game = False

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

  
while input("Do you want to play a game of Blackjack? Yes or No\n").lower() == "yes":
   clear()
   blackjack()


    

