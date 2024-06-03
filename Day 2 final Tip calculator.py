# Tip calculator

#import functions:
import Archive.Stefan_functies as s

def program():
# welcome
    print("Welcome to the tip calculator\n")

    total_bill = s.total_bill_amount()
    tip_percentage = s.tip_percentage_()
    N_people = s.people()
    
    #calculate tip amount        
    tip_amount = total_bill * (tip_percentage / 100)
    #calculate total amount (bill + tip)
    amount = ((total_bill / 100) * (100 + tip_percentage))        
    #calculate amount for each person
    amount_per_person = ((total_bill / 100) * (100 + tip_percentage)) / N_people

    print(f"""
Total bill is ${total_bill:.2f}.
Tip percentage is {tip_percentage}%, which is ${tip_amount:.2f}.
Total amount to pay is ${amount:.2f}.
The bill should be splitt between {N_people} people.
\033[93meach person should pay: ${amount_per_person:.2f}. \033[0m\n"""
    )

    again = input("Do it again? yes or no \n")
    if again == "yes":
        program()

program()

print("\nthanks for using the tip calculator!")