#importing modules
import os
from random import randint

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#define functions
def GAME():
    def clear():
        os.system('cls')

    def CheckGameOverFirstHand():
        if sum(userhand) == 21 and sum(computerhand) == 21:
            return "Draw, double Blackjack!"
        elif sum(userhand) == 21 and sum(computerhand) != 21:
            return "Player wins with Blackjack!"
        elif sum(computerhand) == 21 and sum(userhand) != 21:
            return "Dealer wins with Blackjack!"

    #start setting
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    userhand = []
    computerhand = []
    userhand.append(cards[randint(0,12)])
    userhand.append(cards[randint(0,12)])
    computerhand.append(cards[randint(0,12)])
    computerhand.append(cards[randint(0,12)])

    #Start game
    print(logo)
    print(f"Playerhand: {userhand}, with a score of {sum(userhand)}")
    print(f"Dealerhand: (first card only) {computerhand[0]}")
    #Start game by checking Blackjack for both players
    CheckGameOverFirstHand()
    PlayerDraw = True

    if CheckGameOverFirstHand() in [
        "Draw, double Blackjack!",
        "Player wins with Blackjack!",
        "Dealer wins with Blackjack!",
    ]:
        print(f"Dealer score: {sum(computerhand)}. {CheckGameOverFirstHand()}")
    else:
        print("Players turn!\n\n")
        while sum(userhand) <21:
            if input("Draw a card? 'y' for yes, 'n' for no: ") == 'y':
                userhand.append(cards[randint(0,12)])
                if sum(userhand) == 21:
                    print(f"Playerhand: {userhand}, with a score of {sum(userhand)}")
                    BlackJack = True
                    PlayerDraw = False
                elif sum(userhand) > 21 and 11 in userhand:
                    location = userhand.index(11)
                    userhand[location] = 1
                    print(f"Playerhand: {userhand}, with a score of {sum(userhand)}")
                elif sum(userhand) > 21:
                    print(f"Playerhand: {userhand}, with a score of {sum(userhand)}. You Lose!")
                    PlayerDraw = False
                    break
                elif sum(userhand) < 21:
                    print(f"Playerhand: {userhand}, with a score of {sum(userhand)}")
            else:
                break
        if sum(userhand) == 21:
            print("Blackjack for player!")
        print("\n--------------------\nDealers Turn\n")
    while sum(computerhand) < 17 and sum(userhand) < 21:
        print(f"\nDealerhand: {computerhand}, with a score of {sum(computerhand)}. Dealer draws!")
        computerhand.append(cards[randint(0,12)])
        if sum(computerhand) == 21:
            print("Blackjack for Dealer")
        elif sum(computerhand) > 21 and 11 in computerhand:
            location = computerhand.index(11)
            computerhand[location] = 1
        if sum(computerhand) > 21:
            print(f"Dealerhand: {computerhand}, with a score of {sum(computerhand)}. \n\nPlayer Wins!\n")
    if sum(computerhand) <= 21 and sum(userhand) <= 21:
        if sum(computerhand) == sum(userhand):
            print(f"\nDealer hand: {computerhand}. with a score of: {sum(computerhand)} \nPlayer hand: {userhand}. with a score of: {sum(userhand)}")
            print("Its a Draw!")
        elif sum(computerhand) < sum(userhand):
            print(f"\nDealer hand: {computerhand}. with a score of: {sum(computerhand)} \nPlayer hand: {userhand}. with a score of: {sum(userhand)}")
            print("Player Wins!")
        elif sum(computerhand) > sum(userhand):
            print(f"\nDealer hand: {computerhand}. with a score of: {sum(computerhand)} \nPlayer hand: {userhand}. with a score of: {sum(userhand)}")
            print("Dealer wins!")
    if input("\n\nWant to play again? 'y' for yes, 'n' for no: ") == "y":
        clear()
        GAME()
    else:
        clear()

GAME()