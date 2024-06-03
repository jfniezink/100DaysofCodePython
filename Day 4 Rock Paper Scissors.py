import random, os, time

def program():
    def clear():
        """Clear terminal screen windows"""
        os.system('cls')

    #define ascii arts in variables
    rock, paper, scissors = '''
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
    ''', '''
    _______
---'   ____)
        ______)
        _______)
        _______)
---.__________)
    ''', '''
    _______
---'   ____)
        ________)
        _________)
        ___)
---.______)
    '''
    #clear screen first
    clear()
    
    #define choises for the game
    choises = [rock, paper, scissors]

    #computers makes a choice
    computer_choice = choises[random.randint(0,2)]

    #welcome screen
    print('''
oooooo   oooooo     oooo           oooo                                                  
 `888.    `888.     .8'            `888                                                  
  `888.   .8888.   .8'    .ooooo.   888   .ooooo.   .ooooo.  ooo. .oo.  .oo.    .ooooo.  
   `888  .8'`888. .8'    d88' `88b  888  d88' `"Y8 d88' `88b `888P"Y88bP"Y88b  d88' `88b 
    `888.8'  `888.8'     888ooo888  888  888       888   888  888   888   888  888ooo888 
     `888'    `888'      888    .o  888  888   .o8 888   888  888   888   888  888    .o 
      `8'      `8'       `Y8bod8P' o888o `Y8bod8P' `Y8bod8P' o888o o888o o888o `Y8bod8P' 
                                                                                                                                                                      
          ''')
    
    #player makes a choise
    valid = False
    while not valid:
        player_choice = input("Rock, Paper or Scrissors?\n").lower()
        if player_choice == 'rock':
            player_choice = rock
            valid = True
        elif player_choice == 'paper':
            player_choice = paper
            valid = True
        elif player_choice == 'scissors':
            player_choice = scissors
            valid = True
        else:
            print("incorrect input")
        
    #print both choises
    print(f'''
Computer made a choice:

{computer_choice}

    ''')
    print(f'''
Player made a choice:

{player_choice}

    ''')

    if player_choice == scissors and computer_choice == rock:
        print("You lose!")
    elif player_choice == paper and computer_choice == rock:
        print("You Win!")
    elif player_choice == rock and computer_choice == paper:
        print("You Lose!")
    elif player_choice == scissors and computer_choice == paper:
        print("You win!")
    elif player_choice == rock and computer_choice == scissors:
        print("You win!")
    elif player_choice == paper and computer_choice == scissors:
        print("You lose!")
    else:
        print("it's a draw!")
        
    again = input("\nWant to play again? 'yes' of 'no'\n").lower()
    if again == 'yes':
        program()
    else:
        print("Thanks for playing!")
        time.sleep(5)
        clear()
        
program()