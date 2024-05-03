import sys
sys.setrecursionlimit(2**31-1)

#generating a deck of cards
def generate_deck()->list:

  sym = [10,20,30,40]
  val = [1,2,3,4,5,6,7,8,9,9.1,9.2,9.3,9.4]
  cards = []


  for i in sym:
    for j in val:
      cards.append(i+j)

  return cards




# distrubution of cards to players
def distribute_cards(cards:list,n_hands:int)-> list[list]:

    if n_hands <=0 and n_hands>52:
      return 'please enter valid number of members'

    deck = []

    for i in range(n_hands):
      deck.append([])

    while len(cards)>0:
      for i in range(n_hands):
        if len(cards)>0:
          deck[i].append(cards[0])
          cards.pop(0)


    for i in range(n_hands):
      deck[i] = sorted(deck[i])
    return deck



# checking no of players are empty

def empty(deck,n_hands):
  a = 0
  for i in range(n_hands):
    if len(deck[i])!=0:
      a+=1
  return a

# checking first round position
def find_posi(deck,n_hands):
  ind = -1
  suit = 10

  for i in range(n_hands):

    if 19.4 in deck[i]:
      ind = i
      
  return(ind,suit)

# Staring the game

def game(deck,start,suit,n_hands):
  start = start
  suit = suit
  play = []
  ans = []
  eam = empty(deck,n_hands)
  

  if eam>=2:
    for i in range(n_hands):
      if len(deck[start])!=0:
        for j in range(len(deck[start])):
          if deck[start][j]>=suit+1 and deck[start][j]<=(suit+9.4):
            play.insert(start,(deck[start][j]))
            ans.insert(start,round((deck[start][j])%10,1))
            
          
            deck[start].remove(deck[start][j])

          
            start = (start+1) % n_hands
            break
          
          elif(j==len(deck[start])-1):
            play.insert(start,(deck[start][-1]))
            ans.insert(start,round((deck[start][j])%10,1))
            
            deck[start].remove(deck[start][-1])
            start = (start+1) % n_hands
          
      else:
        start = (start+1) % n_hands
      
      




    Min = min(play)
    Max = max(play)
    Maxi = max(ans)
    # test case for checking tie
    if ans.count(Maxi)>=2:
      ind = play.index(Max)
      if Min>=suit+1 and Max<=suit+9.4:
        play = []
        ans = []

        suit = (int(deck[ind][0])//10)*10
        
        return game(deck,ind,suit,n_hands)
      # test for players has different suits
      else:
        deck[ind]+=play
        deck[ind] = sorted(deck[ind])
        suit = (int(deck[ind][0])//10)*10
        
        return game(deck,ind,suit,n_hands)


    # checking cards are in same suit 
    else:
      ind = ans.index(Maxi)
      
      if Min>=suit+1 and Max<=suit+9.4:
        play = []
        ans = []

        suit = (int(deck[ind][0])//10)*10
        
        return game(deck,ind,suit,n_hands)
      # checking cards are in different suits
      else:
        deck[ind]+=play
        deck[ind] = sorted(deck[ind])
        suit = (int(deck[ind][0])//10)*10
        
        return game(deck,ind,suit,n_hands)

  # declaring the looser
  else:
    for i in range(n_hands):
      if len(deck[i])!=0:
        
        return i,deck[i]




cards = generate_deck()
n_hands = 5
import random
random.seed(5)
random.shuffle(cards)
hands = distribute_cards(cards, n_hands)


a,b = find_posi(hands,n_hands)

losser,hand = game(hands,a,b,n_hands)
#changing numbers to codes/card values
symbols = {1:'S',2:'H',3:'C',4:'D'}
values = {1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'10',9.1:'J',9.2:'Q',9.3:'K',9.4:'A'}
ans_hand = []
for i in hand:
  ans_hand.append(symbols[int(i//10)]+values[round(i%10,1)])

#printing loosers
print(losser)
print(ans_hand)



