from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

# function to check users's guess against actual answer.
def check_answer(guess,answer,turns):
    """check answer against guess. Returns the number of turns remaining"""
    if guess> answer:
        print("Too high.")
        return turns -1
    elif guess<answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You Got It! the answer was {answer}.")

# Make function to set difficulity 

def set_diificulty():
    level= input("Choose a diificulty. Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    # choosing a random number 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm Thinking of a number between 1 and 100.")
    answer= randint(1,100)
    turns = set_diificulty()
    guess =0 
    while guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number.")  
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return 
        elif guess!= answer:
            print("Guess Again.")

game()