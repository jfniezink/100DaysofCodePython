#importing modules
import Hangman_art, Hangman_words, random, os, time

def hangman():
    #set starting N of lives
    lives = 6

    #welcome the player and display the hang
    print("Welcome to a game of HANGMAN!\n")
    print(Hangman_art.logo)

    #pick a random word for the user to guess
    word_to_guess = random.choice(Hangman_words.word_list)

    #Create a list containing letters from the word_to_guess
    word_to_guess_list = []
    for letter in word_to_guess:
        word_to_guess_list.append(letter)

    #Create a list for the guesses. Every letter in the guess word list will be one '_'
    user_guess_list = []
    for letter in word_to_guess:
        user_guess_list.append("_")

    #create a list for allready guesses letters
    previous_guesses = []
    
    while "_" in user_guess_list and lives != 0:
        print(Hangman_art.stages[lives])
        print(user_guess_list)
        
        #Take user input for a letter to guess, must be a letter. 
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        guess = input("Guess a letter: ").lower()
        while guess not in alphabet:
            guess = input("Wrong input.. Guess a letter: ").lower()
        
        os.system("cls")
        
        #see if the guess is in the word, otherwise take a life except if the guess has already been made. 
        if guess not in previous_guesses:
            correct = False
            for letter in word_to_guess_list:
                if letter == guess:
                    user_guess_list[word_to_guess_list.index(letter)] = letter
                    word_to_guess_list[word_to_guess_list.index(guess)] = "1"
                    correct = True
            if not correct:
                print(f"{guess} is not in the word. You lose a life!")
                lives -= 1
            else:
                print(f"{guess} is in the word!")
        else:
            print(f"{guess} has already been guessed.")
                
        #add the guess to previous_guesses
        previous_guesses.append(guess)

    print(Hangman_art.stages[lives])
    if "".join(user_guess_list) == word_to_guess:
        print(f"You win! the word was {word_to_guess}")
    else:
        print(f"you lose, the word was {word_to_guess}")
    
    choise = ['y','n']
    again = input("wanna play again? 'y' or 'n'\n").lower()
    while again not in choise:
        again = input("please input 'y' or 'n'\n").lower()        
    if again == 'y':
        os.system("cls")
        hangman()
    else:
        print("thanks for playing!")
        
hangman()

