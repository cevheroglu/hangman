import random
from arts import stages, logo
from word_list import word_list

print(logo)
display = []
selected_letters = []
word = random.choice(word_list)
#print(word)

for letter in word:
    display.append("_")
print(" ".join(display))

z=list(word)
lives = 6

while not display  == z:
    guess = input("\nGuess a letter ").lower()
    a = -1
    if guess in selected_letters:
        print("YOU ALREADY TRIED THIS LETTER")
    elif guess not in word:
        selected_letters.append(guess)
        print(selected_letters)
        if lives == 1:
            print(stages[0])
            print("YOU LOST")
            print(word)
            quit()
        else:
            lives -= 1
            print(" ".join(display))
            print(stages[lives])
    else:#elif guess in word:
        selected_letters.append(guess)
        print(selected_letters)
        for y in word:
            a += 1
            if y == guess:
                display[a] = guess
        print(" ".join(display))
        print(stages[lives])

print(" ".join(display))
print(" \nYOU WON!!!\nYOU ARE AN INCREDIBLE HUMAN BEING!!!\n\n")
