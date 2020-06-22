# This is a Guess the Number game.
import random

guessTakenn = 0

print("Hi! What is your name")
myName = input()

number = random.randint(1,20)
print(f"Well, {myName}, I am thinking of a number between 1 and 20")

for guessTakenn in range(6):
    print("Take a guess.")

    guess = input()
    guess = int(guess)

    if guess < number:
        print(f"Your guess is too low, {myName}.")

    elif guess > number:
        print(f"Oh! {myName}, your guess is too high dude.")

    elif guess == number:
        break

if guess == number:
    guessTakenn = str(guessTakenn + 1)
    print(f"Nice One {myName}, You guessed my number in {guessTakenn} guesses")

elif guess != number:
    number = str(number)
    print(f"nah {myName}. I was actually thinking of {number}")
