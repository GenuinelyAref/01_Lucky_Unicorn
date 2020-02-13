# Lucky Unicorn Decomposition Step 3
# Generate a random token

# To do
# Set up starting amount
# Choose 100 tokens
#  count # of unicorns and multiply by 5
#  count # of horse / zebra and multiply by 0.5
#  count # of donkeys
#  work out total won / lost

import random

HOW_MUCH = 100
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey", "unicorn"]

unicorn_count = 0
zebhor_count = 0
donkey_count = 0

for item in range(0,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1
    elif chosen == "donkey":
        donkey_count += 1
    else:
        zebhor_count += 1



    print(chosen)

# Money Calculations ...
winnings = unicorn_count * 5 + zebhor_count * 0.5


print(chosen)
print()
print("**** Win / Loss Calculations ****")
print()
print("# Unicorns: {}".format(unicorn_count))
print("# Zebras / Horses: {}".format(zebhor_count))
print("# Donkeys: {}".format(donkey_count))

print()
print("You spent ${}".format(HOW_MUCH))
print("You go home with ${:.2f}".format(winnings))