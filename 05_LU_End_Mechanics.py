# Lucky unicorn - payment mechanics

# To do
# Aak user how much money they have to play with
# If the total is less than $1, quit
# If the total is more than $1, ask user of they want to keep going


# Assume starting amount is $10
total = int(input("How much would you like to play with? "))

keep_going = ""
while keep_going == "":

    # Allow manual token input for testing purposes
    token = input("enter a token: ")

    # Adjust total correctly for a given token
    if token == "unicorn":
        total += 5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        total -= 1
        feedback = "Sorry, you did not win anything this round"
    else:
        total -= 0.5
        feedback = "Congratulations you won 50c"

    print()

    print(feedback)
    print("You have {} to play with".format(total))

    if total < 1:
        print("Sorry you don't enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")
