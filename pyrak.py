from getch import getch
from termcolor import colored
from constants import *
from fetchWords import *
import random
import sys

ARTICLES = ["cat", "dog", "haskell", "python", "glass"]

def main():
  a = random.randint(0, len(ARTICLES)-1)
  print("Welcome to Dvorak practice!")
  print("--------------------")
  print(f"Starting a practice session on article {ARTICLES[a]}...\n")

  checkArticle(ARTICLES[a])

  print("Session finished.")

def check(word):
  print(f"{word}")
  for wordChar in list(word):
    userChar = getch()
    if(userChar != wordChar):
      print(colored(f"\nError: '{userChar}' in {word}", 'red'))
      print(colored(f"(expected {wordChar}); Press y to continue.", 'yellow'))
      while (userChar != 'y'):
        userChar = getch()
      return
    print(colored(userChar, 'green'), end='')

  print(colored("✓\n", 'green'))

def checkArticle(article):
    rated = rateArticle(article)
    sentences = [ a[0] for a in rated ]
    list(map(check, sentences))

# Disable buffering
# (https://stackoverflow.com/questions/107705/disable-output-buffering)
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

if __name__ == "__main__":
    main()
