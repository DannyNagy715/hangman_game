#imorting random library
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
lives = 6
end_game = False

#random word generation
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.stages[6])
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
        print(f"Your guess {guess} is not in the word. You lost a life :(")
        print(hangman_art.stages[lives])
        if lives == 0:
            end_game = True
            print("You lost")
            

    if "_" not in display:
        end_game = True
        print("You win")
        
        

    print(f"{' '.join(display)}")
