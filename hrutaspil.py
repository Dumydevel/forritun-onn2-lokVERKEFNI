from random import shuffle
from random import randint

class Card(object):
    names = ["Name", "Weight", "Milk", "Cotton", "Offspring", "Leg score", "Fertility", "Spine score", "Back score"]

    def __init__(self, values):
        self.values = values
        self.name = values[0]
        
    def __str__(self):
      v = ""
      for i in range(0, 9):
        v += str(i) + " " + str(Card.names[i]).ljust(11) + " =\t" + str(self.values[i]) + "\n"
      return v

# Reads in the cards info from a file.
# Retuns 52 cards in a array.
def readInCards(textfile):
    cards = []
    with open(textfile, 'r', encoding = 'utf-8') as f:
        for line in f: 
            values = readInCard(line)
            s = Card(values) 
            cards.append(s)
    return cards

# This takes in the array and splits it into card components
# Example of a line:
#    Gotti;47.2;100;8.0;182;17.5;102;119;8.6
def readInCard(line):
    arr = line.split(";")
    val = []
    val.append(arr[0])
    for i in range(1, 9):
      val.append(float(arr[i]))
    return val


entireDeck = readInCards("spilabunki.txt")
shuffle(entireDeck)
playerDeck = []   # Deck for the player
computerDeck = [] # Deck for the computer
tieDeck = []     # Used to keep cards when there is a tie


def Play():
  for i in range(0,26):
    playerDeck.append(entireDeck[i])
  for i in range(26,52):
    computerDeck.append(entireDeck[i])
  
  playersTurn = randint(0,1) == 0
  turns = 0
  isPlaying = True
  while len(playerDeck) > 0 and len(computerDeck) > 0 and isPlaying:
    turns += 1
    print("----------------------------- TURN " + str(turns) + " -----------------------------")
    print("Players Deck: " + str(len(playerDeck)) + "\t Computers Deck: " + str(len(computerDeck)) + "\t Tied Deck: " + str(len(tieDeck)))
    if (playersTurn):
      isPlaying = PlayersTurn()
      playersTurn = False
    else:
      ComputerTurn()
      playersTurn = True
  
  if isPlaying:
    print("----------------------------- TURN " + str(turns) + " -----------------------------")
    print("Players Deck: " + str(len(playerDeck)) + "\t Computers Deck: " + str(len(computerDeck)) + "\t Tied Deck: " + str(len(tieDeck)))
    if len(playerDeck) == 0:
      print("The player won the game!")
    else:
      print("The computer won the game!")
  else:
    print("Thank you, come again!")

def ComputerTurn():
  choice = randint(1,8)
  compValue = computerDeck[0].values[choice]
  playerValue = playerDeck[0].values[choice]
  print("Computer picked " + Card.names[choice])
  print("Your card: " + playerDeck[0].name + " has " + str(playerValue))
  print("Computer card: " + computerDeck[0].name + " has " + str(compValue))
  resolve_battle(compValue,playerValue)
  

def PlayersTurn():
  print("Card at top of deck:")
  print(playerDeck[0])
  choice = -1
  while True:
    val = input("Choose which catagory you want to compete at [1-8] (Or 0 to quit): ")
    if (RepresentsInt(val)):
      choice = int(val)
      if choice >= 0 and choice <= 8:
        break  
    print("Invalid input, Enter a number between 1 and 8")
  
  if choice == 0:
    return False
  else:
    compValue = computerDeck[0].values[choice]
    playerValue = playerDeck[0].values[choice]
    print("Computer card: " + computerDeck[0].name + " which has " + str(compValue) + " in " + Card.names[choice])
    resolve_battle(compValue,playerValue)
  return True
 
def resolve_battle(compValue,playerValue):
  if compValue > playerValue:
    print("Computer Won")
    computerDeck.append(computerDeck.pop(0))
    computerDeck.append(playerDeck.pop(0))
    if len(tieDeck) > 0:
      computerDeck.extend(tieDeck)
      del tieDeck[:]
  elif playerValue > compValue:
    print("Player Won")
    playerDeck.append(computerDeck.pop(0))
    playerDeck.append(playerDeck.pop(0))
    if len(tieDeck) > 0:
      playerDeck.extend(tieDeck)
      del tieDeck[:]
  else:
    tieDeck.append(computerDeck.pop(0))
    tieDeck.append(playerDeck.pop(0))

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

Play()