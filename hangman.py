#imorting random library
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
end_game = False
word_list = ["ardwark", "baboon", "camel"]

#random word generation
chosen_word = random.choice(word_list)
print(f"word is {chosen_word}")


#filling up display list and printing the empty list
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
        
print(f"{' '.join(display)}")

#ask for user input until all letters are filled
while not end_game:

    guess = input("please guess a letter from our word: ").lower()

    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
        
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_game = True
            print("You lost")
            

    if "_" not in display:
        end_game = True
        print("You win")
        
        

    print(f"{' '.join(display)}")
