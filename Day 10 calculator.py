import os

logo = """
 _____________________
|  _________________  |
| | PYTHONISTA   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

#Functions

def program():
    def calculate(n1, n2, operation):
        if operation == "+":
            return n1 + n2
        elif operation == "-":
            return n1 - n2
        elif operation == "/":
            return n1 / n2
        elif operation == "*":
            return n1 * n2
        else:
            return "invalid"

    proceed = True
    
    while proceed:
        print(logo)
        number_1 = float(input("First number?: "))
        operator = input("What operation?\n-\n+\n/\n*\n")
        number_2 = float(input("Second number?: "))
        result = calculate(n1 = number_1, n2 = number_2, operation=operator)

        print(f"{number_1} {operator} {number_2} = {calculate(n1 = number_1, n2 = number_2, operation=operator)}")
        
        go_on = 'y'
        while go_on == 'y':
            go_on = input(f"another operation with current number {result}? 'y' or 'n' \n").lower()
            
            if go_on == 'n':
                os.system("cls")
            
            else:
                operator = input("What operation?\n-\n+\n/\n*\n")
                number_2 = int(input("Second number?: "))
                print(f"{result} {operator} {number_2} = {calculate(n1 = result, n2 = number_2, operation=operator)} ")
                result = calculate(n1 = result, n2 = number_2, operation=operator)

program()