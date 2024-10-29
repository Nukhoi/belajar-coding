#CARD CLASS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
class Card:
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

#DECK CLASS
import random
class Deck:
  def __init__(self):
    self.all_card = []
    for suit in suits:
      for rank in ranks:
        self.all_card.append(Card(suit,rank))
  #Method
  def suffle(self):
    random.shuffle(self.all_card)
  def deal_one(self):
    return self.all_card.pop()
    
#PLAYER CLASS
class Player:
  def __init__(self,name):
    self.name = name
    self.all_card = []
  def remove_one(self):
    return self.all_card.pop(0)
  def add_cards(self,new_cards):
    if type(new_cards) == type([]):
      self.all_card.extend(new_cards)
    else:
      self.all_card.append(new_cards)
  
#WAR GAME LOGIC
Player_one = Player("One")
Player_two = Player("Two")
#SETUP GAME
new_deck = Deck()
new_deck.suffle()
#SPLIT DECK BETWEEN PLAYERS
len(new_deck.all_card)/2
for x in range(26):
  Player_one.add_cards(new_deck.deal_one())
  Player_two.add_cards(new_deck.deal_one())
#PLAY GAME
import pdb
game_on = True
round_num = 0
while game_on:
  round_num += 1
  print(f"Round {round_num}, FIGHT!!!")
  if len(Player_one.all_card) == 0:
    print("Player One out of card! GAME OVER!")
    print("Player Two WINS!!!")
  if len(Player_two.all_card) == 0:
    print("Player Two out of card! GAME OVER!")
    print("Player One WINS!!!")
    game_on = False
    break
  #NEXT ROUND with card on the table
  Player_one_cards = []
  Player_one_cards.append(Player_one.remove_one())
  Player_two_cards = []
  Player_two_cards.append(Player_two.remove_one())
  
  at_war = True
  while at_war:
    if Player_one_cards[-1].value > Player_two_cards[-1].value:
      Player_one.add_cards(Player_one_cards)
      Player_one.add_cards(Player_two_cards)
      at_war = False
    elif Player_one_cards[-1].value < Player_two_cards[-1].value:
      Player_two.add_cards(Player_one_cards)
      Player_two.add_cards(Player_two_cards)
      at_war = False
    else:
      print("!!! WAR !!!")
      #print(f'Player One : {Player_one_cards}')
      #print(f'Player Two : {Player_two_cards}')
      if len(Player_one.all_card) < 5:
        print("Player One unable to play war! Game Over at War")
        print("Player Two Wins! Player One Loses!")
        game_on = False
        break
      elif len(Player_two.all_card) < 5:
        print("Player Two unable to play war! Game Over at War")
        print("Player One Wins! Player One Loses!")
        game_on = False
        break
      else:
        for num in range(5):
          Player_one_cards.append(Player_one.remove_one())
          Player_two_cards.append(Player_two.remove_one())
          