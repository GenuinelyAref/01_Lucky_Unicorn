# Lucky unicorn - payment mechanics

# To do
# Allow manual token input for testing purposes
# Adjust total correctly for a given token
#   - if it's a unicorn, add $5
#   - if it's a zebra /horse, subtract 0.5
#   - if it;s a donkey, subtract 1
# Give user feedback based on winnings...
# State new total

# Assume starting amount is $10
total = 10

# Allow manual token input for testing purposes
token = input("enter a token: ")

# Adjust total correctly for a given token
if token == "unicorn":
    total +=5
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