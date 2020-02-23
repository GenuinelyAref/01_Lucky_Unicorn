# Lucky Unicorn Decomposition Step 1
# Program should work - needs to be tested for usability

import random


# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "Whoops! Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
            print()

# Statement Generator
def statement_gen(statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))
          

# Main Routine Goes here...

# Set up Initial variables and lists
Rounds_played = 0

# tokens list that includes 10 times to prevent too many unicorns being chosen
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey", "unicorn"]

# **** Introduction *****
print("\n"
                   "\033[1m\033[44;37m**** Welcome to the Lucky Unicorn Game **** \033[m\033[0m \n" +
                   "\nThis game is designed to help the charity 'Bricks for India'. All processed money is transferred "
                   "directly to the non-profit organisation. \n"

                   "A random token is generated each round, and based on it, will be the amount of money you earn.\n"
                   "\n\033[1mTo play, enter an amount of money between $1 and $10 (whole dollars only). \033[0m\n\n"
                   "- Each round costs $1 \n \n"
                   "\033[1m\033[44;46mPayouts... \033[m\n"
                   "- Unicorn: $5.00 \n"
                   "- Horse / Zebra: $0.50 \n"
                   "- Donkey: $0.00 \033[0m\n \n \n")

print()

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with?: $ ", 1, 10)

keep_going = ""
while keep_going == "":

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    Rounds_played += 1
    print()

    # Adjust total correctly for a given token
    if token == "unicorn":
        balance += 5
        feedback = statement_gen("## Congratulations! You got a unicorn. You won $5.00 ##", "#")       
                    
    elif token == "donkey":
        balance -= 1
        feedback = statement_gen("-- Sorry. You got a donkey. You did not win anything this round --", "-")       

    elif token == "horse":
        balance -= 0.5
        feedback = statement_gen("^^ Sorry. You got a horse. You won back 50c from your $1 ^^ ", "^") 

    else:
        balance -= 0.5
        feedback = statement_gen("^^ Sorry. You got a zebra. You won back 50c from your $1 ^^ ", "^") 

    print()
    print(feedback)
    print("Rounds played: {}".format(Rounds_played) +
                    "\t \t \t  Balance: ${:.2f}".format(balance))
    print()

    if balance < 1:
        print("Sorry you don't enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit\n\n")

print("Thank you for playing. ")
