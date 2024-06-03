#password generator

#import modules
import os, random, time

#functions
def clear():
    """Clear terminal screen windows"""
    os.system('cls')

def rust(x):
    """Takes in floats for the terminal to do nothing"""
    time.sleep(x)

def password_generator():
    #welcome screen
    logo = '''
_______     __        ________  ________  __   __  ___     ______     _______   ________           
|   __ "\   /""\      /"       )/"       )|"  |/  \|  "|   /    " \   /"      \ |"      "\          
(. |__) :) /    \    (:   \___/(:   \___/ |'  /    \:  |  // ____  \ |:        |(.  ___  :)         
|:  ____/ /' /\  \    \___  \   \___  \   |: /'        | /  /    ) :)|_____/   )|: \   ) ||         
(|  /    //  __'  \    __/  \\   __/  \\   \//  /\'    |(: (____/ //  //      / (| (___\ ||         
/|__/ \  /   /  \\  \  /" \   :) /" \   :)  /   /  \\   | \        /  |:  __   \ |:       :)         
(_______)(___/    \___)(_______/ (_______/  |___/    \___|  \"_____/   |__|  \___)(________/          
                                                                                                    
_______    _______  _____  ___    _______   _______        __  ___________  ______     _______      
/" _   "|  /"     "|(\"   \|"  \  /"     "| /"      \      /""\("     _   ")/    " \   /"      \     
(: ( \___) (: ______)|.\\   \    |(: ______)|:        |    /    \)__/  \\__/// ____  \ |:        |    
\/ \       \/    |  |: \.   \\  | \/    |  |_____/   )   /' /\  \  \\_ /  /  /    ) :)|_____/   )    
//  \ ___  // ___)_ |.  \    \. | // ___)_  //      /   //  __'  \ |.  | (: (____/ //  //      /     
(:   _(  _|(:      "||    \    \ |(:      "||:  __   \  /   /  \\  \\:  |  \        /  |:  __   \     
\_______)  \_______) \___|\____\) \_______)|__|  \___)(___/    \___)\__|   \"_____/   |__|  \___)    
\n\n'''
    print(logo)
    #Get user to input N of characters in password
    valid = False
    while not valid:
        letters = input("How many letters would you like in your password?\n")
        try: 
            int(letters)
            valid = True
            letters = int(letters)
        except:
            print("please use numbers")
            
    #Get user to input N of symbols in password
    valid = False
    while not valid:
        symbols = input("How many symbols would you like in your password?\n")
        try: 
            int(symbols)
            valid = True
            symbols = int(symbols)
        except:
            print("please use numbers")
            
    #Get user to input N of numbers in password
    valid = False
    while not valid:
        numbers = input("How many numbers would you like in your password?\n")
        try: 
            int(numbers)
            valid = True
            numbers = int(numbers)
        except:
            print("please use numbers")

    #Lists with items for password generation:
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Create a random password using item lists:
    password = []
    for letter in range(1,letters +1):
        password.append(letters_list[random.randint(0,len(letters_list)-1)])
    for number in range(1,numbers +1):
        password.append(numbers_list[random.randint(0,len(numbers_list)-1)])
    for symbol in range(1,symbols +1):
        password.append(symbols_list[random.randint(0,len(symbols_list)-1)])

    #shuffle items in the list
    random.shuffle(password)
    #create a string from the list
    password = ''.join(password)

    #Give user the generated password to copy within 5 seconds:
    print(f"Here is your password: {password}")
    print("copy password before screen clears... in..")
    for second in range(10,0,-1):
        print(second)
        rust(1)
    clear()
    
    #ask user to generate again. if no, quit
    again = input("\nWant to generate another password? 'yes' of 'no'\n").lower()
    if again == 'yes':
        password_generator()
    else:
        print("Ending..")
        for i in range(2): rust(i)
        clear()

password_generator()