# Lucky Unicorn Decomposition Step 1
# Get initia; amount and check that it's valid

# Integer checking function
def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Please enter an integer between {} " \
                    "and {}".format(low,high)

            try:
                response = int(input("Enter an integer between {} "
                                     "and {}: ".format(low,high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)
                print()

# main routine goes here

how_much = intcheck("Enter a number between 1 and 10",1,10)
