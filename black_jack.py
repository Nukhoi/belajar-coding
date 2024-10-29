import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True
class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]
  def __str__(self):
    return self.rank + " of " + self.suit
  
class Deck:
  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))
      
  def __str__(self):
    deck_composition = ''
    for card in self.deck:
      deck_composition += '\n'+ card.__str__()
    return 'The deck has:'+ deck_composition
  def shuffle(self):
      random.shuffle(self.deck)
  def deal(self):
    single_card = self.deck.pop()
    return single_card

class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0
  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == 'Ace':
      self.aces += 1
  def adjust_for_ace(self):
    while self.value > 21 and self.aces > 0:
      self.value -= 10
      self.aces -= 1

class Chips:
  def __init__(self,awal=1000):
    self.awal = awal
    self.bet = 0
  def win_bet(self):
    self.awal += self.bet
  def lose_bet(self):
    self.awal -= self.bet

def take_bet(chips):
  while True:
    try:
      chips.bet = int(input('Mau taruhan berapa chips?'))
    except:
      print('ketikan angka!!!')
    else:
      if chips.bet > chips.awal:
        print('Sorry chips lo ga cukup bos! Chips Lo: {}'.format(chips.awal))
      else:
        break

def hit(deck,hand):
  single_card = deck.deal()
  hand.add_card(single_card)
  hand.adjust_for_ace()
def hit_or_stand(deck,hand):
  global playing
  while True:
    O = input('\n Hit atau Stand? H or S')
    if O[0].upper() == 'H':
      hit(deck,hand)
    elif O[0].upper() == 'S':
      print('Player stand bandar jalan')
      playing = False
    else:
      print('yang bener H atau S')
      continue
    break

def show_some(player,dealer):
  print("\n Kartu bandar: ")
  print("\n Kartu pertama bandar ditutup! ")
  print(dealer.cards[1])
  print("\n Kartu ditangan pemain: ")
  for card in player.cards:
    print(card)
def show_all(player,dealer):
  print("\n Kartu bandar: ")
  for card in dealer.cards:
    print(card)
  print(f'\n Nilai kartu bandar adalah: {dealer.value}')
  print("\n Kartu ditangan pemain: ")
  for card in player.cards:
    print(card)
  print(f'\n Nilai kartu lo adalah: {player.value}')
  
def player_busts(player,dealer,chips):
  print("\n BUST PLAYER!")
  chips.lose_bet()
def player_wins(player,dealer,chips):
  print("\n PLAYER WINS!")
  chips.win_bet()
def dealer_busts(player,dealer,chips):
  print("PLAYER WINS! DEALER BUSTED!")
  chips.win_bet()
def dealer_wins(player,dealer,chips):
  print("DEALER WINS!")
  chips.lose_bet()
def push(player,dealer):
  print("Dealer and Player tie! PUSH")

while True:
  print("###### WELCOME TO BLACKJACK ######")
  deck = Deck()
  deck.shuffle()
  print("###### KARTU DIKOCOK ######")
  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())
  print("### KARTU PEMAIN DIBAGIKAN ###")
  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())
  print("### KARTU DEALER DIBAGIKAN ###")
  
  player_chips = Chips()
  take_bet(player_chips)
  show_some(player_hand,dealer_hand)
  while playing:
    hit_or_stand(deck,player_hand)
    show_some(player_hand,dealer_hand)
    if player_hand.value > 21:
      player_busts(player_hand,dealer_hand,player_chips)
      break
  if player_hand.value <= 21:
    while dealer_hand.value < 17:
      hit(deck,dealer_hand)
    show_all(player_hand,dealer_hand)
    if dealer_hand.value > 21 :
      dealer_busts(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value > player_hand.value:
      dealer_wins(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand,dealer_hand,player_chips)
    else:
      push(player_hand,dealer_hand)
  print("\n Total chips kamu adalah: {}".format(player_chips.awal))
  
  new_game = input("MAU MAIN LAGI? Y/N")
  if new_game[0].upper() == 'Y':
    playing = True
    continue
  else:
    print("AHH DASAR LEMAH!!!")
    break