# Lucky Unicorn Decomposition Step 2
# Generate a random token

import random

tokens = ["horse", "zebra", "donkey", "unicorn"]

for item in range(1,15):
    chosen = random.choice(tokens)
    print(chosen)
