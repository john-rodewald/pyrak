from enum import Enum
from getch import getch
from termcolor import colored
import random

AMOUNT      = 3
TOPROW      = list("pyfgcrl")
HOMEROW     = list("aoeuidhtns")
BOTTOMROW   = list("qjkxbmwvz")
PATH        = "words.txt"

option = {
  0: "random",
  1: "home",
  2: "top",
  3: "bottom"
}

def main():
  print("Welcome to Dvorak practice!")
  print("--------------------")
  print("(1) Practice random words | (2) Practice homerow words | (3) Practice home/top row words | (4) Practice home/bottom row words")
  o = getOption()
  words = selectWords(option[o])
  print(f"Starting a practice session with {AMOUNT} random words...\n")
  for word in words:
    check(word)
  print("Session finished.")

def check(word):
  print(f"{word}")
  for wordChar in list(word):
    userChar = getUserChar()
    if(userChar != wordChar):
      print(f"{colored(f'Error: {userChar} in {word}','red')} {colored(f' (expected {wordChar})','yellow')}\n")
      return
    print(colored(userChar, 'green'))

  print(colored("✓\n", 'green'))

def selectWords(option):
  allWords = readRandomWords()
  if(option == "random"):
    words = random.choices(allWords, k=AMOUNT)
    return words
  elif(option == "home"):
    words = [ word for word in allWords if all(c in HOMEROW for c in list(word)) ]
  elif(option == "top"):
    words = [ word for word in allWords if all(c in (HOMEROW + TOPROW) for c in list(word)) ]
  elif(option == "bottom"):
    words = [ word for word in allWords if all(c in (HOMEROW + BOTTOMROW) for c in list(word)) ]
  return take(AMOUNT, words)

def readRandomWords(filepath=PATH):
  with open(filepath) as infile:
    lines = infile.readlines()
    random.shuffle(lines)
    return stripList(lines)

# Helper functions
def stripList(l):
  return list(map(lambda w: w.strip(), l))

def take(n, l):
  return l[:n]

def getOption():
  try: 
    i = int(getch()) - 1
  except:
    print("Invalid option.")
    exit()
  return i

def getUserChar():
  userChar = getch()
  while(not userChar.isalpha()):
      userChar = getch()
  return userChar

if __name__ == "__main__":
    main()
