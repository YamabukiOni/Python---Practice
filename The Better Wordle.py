#Title
game_title = "The Better Wordle"
print(game_title)
print("bet you suck")
max_turns = 5
turns_taken = 0
print ("you have " + str(max_turns - turns_taken) + " turns left")



word_bank = ['apple', 'watch', 'house', 'table', 'cause',
              'breed', 'bread', 'clean', 'break', 'black',
                'clock', 'drive', 'joust', 'value', 'zebra',
                 'quick']

import random
random.choice(word_bank)

incorrect_guesses = ["red"]
misplaced_guesses = ["yellow"]
correct_guesses = ["green"]
max_turns = 5
turns_taken = 0

while turns_taken < max_turns:
    guesss = input("Guess the damn word: ").lower()

index = 0
    for c in guess: # type: ignore
        if c == word_to_guess[index]: # type: ignore
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess: # type: ignore
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")
        index += 1

    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    turns_taken += 1

    while True:
    user_word = input("Guess the damn word: ")
    if len(user_word) == 5 and any(guess in user_word for guess in incorrect_guesses):
        print("womp womp")
    if len(user_word) == 5 and any(guess in user_word for guess in misplaced_guesses):
        print("wrong side of the world")
    if len(user_word) == 5 and any(guess in user_word for guess in correct_guesses):
        print("It is.. acceptable")
    if len(user_word) != 5:
        print("5 letters, still more than your total amount of braincells")

    if user_word == random.choice(word_bank):
        print("Impressive")
    break 

    if user_word != random.choice(word_bank):
      print("failure")
    break