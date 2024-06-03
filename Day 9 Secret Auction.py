#Secret Auction program

#imports
import os

logo = '''
            ___________
            \         /
            )_______(
            |"""""""|_.-._,.---------.,_.-._
            |       | | |               | | ''-.
            |       |_| |_             _| |_..-'
            |_______| '-' `'---------'` '-'
            )"""""""(
            /_________\\
        .-------------.
        /_______________\\
'''
#Start and welcome
print(logo)
print("Welcome to the secret auction program.")

#function to find highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")

#create empty dictionary to add bids
bidders = {}

go_on = True
while go_on:
    name = input("What is your name?: \n")
    bid = float(input("What's your bid?: \n"))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? type 'yes' or 'no' \n")
    if more_bidders == 'yes':
        os.system("cls")
    else:
        go_on = False
        os.system("cls")
        find_highest_bidder(bidders)