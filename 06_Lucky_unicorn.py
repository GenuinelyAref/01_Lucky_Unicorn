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

# main routine goes here

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? ", 1,10)

keep_going = ""
while keep_going == "":

    # tokens list that includes 10 times to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust total correctly for a given token
    if token == "unicorn":
        balance +=5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        balance -= 1
        feedback = "Sorry, you did not win anything this round"
    else:
        balance -= 0.5
        feedback = "Congratulations you won 50c"

    print()

    print(feedback)
    print("You have ${:.2f} to play with".format(balance))
    print()

    if balance < 1:
        print("Sorry you don't enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

print("Thank you for playing. ")