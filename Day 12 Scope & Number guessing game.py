# Number Guessing game

#Modules
import random, os

def clear():
    os.system("cls")

#welcome text
WELCOME_TXT = """
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""
START_TXT = "I'm thinking of a number between 1 and 100"
DIFFICULTY = "Choose a difficulty. Type 'easy' or 'hard': "

def GAME():
    clear()
    print(WELCOME_TXT)
    print(START_TXT)

    valid = False
    while not valid:
        level = input(DIFFICULTY).lower()
        if level == 'easy':
            guesses = 10
            valid = True
        elif level == 'hard':
            guesses = 5
            valid = True

    number = random.randint(1,100)
    # print(f"its {number}")

    guessed = False

    while not guessed and guesses > 0:
        print(f"You have {guesses} attemps remaining to guess the number.")
        valid_guess = False
        while not valid_guess:
            x = input("Make a guess: ")
            try: 
                x = int(x)
                valid_guess = True
            except ValueError:
                print("please provide a number between 0 and 100")
        guesses -= 1
        if x == number:
            guessed = True
        elif x < number:
            print("To low.")
            if guesses > 0:
                print("Guess again.")
        elif x > number:
            print("To high.")
            if guesses > 0:
                print("Guess again.")

    if guessed:
        print(f"You got it! The answer was {number}")
    elif not guessed and guesses == 0:
        print("You've run out of guesses, you lose")
        
    if input("\n\nWant to play again? 'y' for yes, 'n' for no: ") == "y":
        GAME()
    else:
        clear()

GAME()