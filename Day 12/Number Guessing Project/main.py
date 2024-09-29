import random

# Welcome message

# Ask if user wants to do easy or hard mode

# Make 2 separate while loops, one for easy mode and one for hard mode depending
# on what user chooses

# Create a random number between 1 and 100

random_num = random.randint(1,100)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()

if difficulty == "easy":
    i = 10
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_num:
            print(f"You got it! The answer is {random_num}")
        elif i > 1 and guess > random_num:
            print("Too High.")
            print("Guess again.")
        elif i > 1 and guess < random_num:
            print("Too low.")
            print("Guess again.")
        i -= 1
    print("You've run out of guesses, you lose")
elif difficulty == "hard":
    i = 5
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_num:
            print(f"You got it! The answer is {random_num}")
        elif guess > random_num:
            print("Too High.")
            print("Guess again.")
        elif guess < random_num:
            print("Too low.")
            print("Guess again.")
        i -= 1
    print("You've run out of guesses, you lose")

#######################################################################
###############################Answer Key##############################
#######################################################################
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    if user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")