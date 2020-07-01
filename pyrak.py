from getch import getch
import random
import time
from termcolor import colored

AMOUNT = 15

def main():
  print("Welcome to Dvorak practice!")
  print(f"Starting a practice session with {AMOUNT} words...")
  print("--------------------")
  practice()
  print("Session finished.")

def practice():
  for word in selectRandomWords('words.txt'):
    check(word)

def check(word):
  print(f"{word}")
  for wordChar in list(word):
    userChar = getch()
    while(not userChar.isalpha()):
        userChar = getch()
    if(userChar != wordChar):
      print(f"{colored(f'Error: {userChar} in {word}','red')} {colored(f' (expected {wordChar})','yellow')}\n")
      return
    print(colored(userChar, 'green'))

  print(colored("✓\n", 'green'))

def selectRandomWords(filepath):
  words: int = []
  with open(filepath) as infile:
    lines = infile.readlines()
    words = random.choices(lines, k=AMOUNT)
  return list(map(lambda w: w.strip(), words))

if __name__ == "__main__":
    main()
