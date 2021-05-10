import random
import hangman_art
import hangman_words
from replit import clear

stages = hangman_art.stages
print(hangman_art.logo)
words_list = hangman_words.word_list
display = []
guessed_words = []
chosen_word = random.choice(words_list)

#Generate blanks
for letter in chosen_word:
    display.append("_")  

correct_guesses = 0
lives = 6

#Loops until the word is correctly guessed
#Or lives run out(checked by if condition down below)
while correct_guesses != len(chosen_word):
  guess = input("Guess a letter: ").lower()
  clear()
  guessed_correctly = False

  #Checks if user guessed correctly
  for i in range(len(chosen_word)):
      if guess == chosen_word[i] and guess not in guessed_words:
        display[i] = guess
        correct_guesses += 1
        guessed_correctly = True 

  #lets the user know that they have already guessed a particular word
  if guess in guessed_words:
    print(f"You already guessed {guess}")

  #Checks if the user guessed a wrong word
  #And the word is not already guessed
  if guessed_correctly == False and guess not in guessed_words:
    print(f"You guessed {guess}, that is not in the word. You lose a life")
    lives -= 1

  if lives == 0:
    print(f"You lose\n\nThe word was: {chosen_word}")
    break 

  if correct_guesses == len(chosen_word):
    print("You win")
    break

  print(*display, sep = ' ')
  print(stages[lives])

  #keeps a track of guessed words
  guessed_words.append(guess) 

            