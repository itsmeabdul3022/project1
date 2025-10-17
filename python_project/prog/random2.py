#using libraries/modules in python
import random
# from random import choice  # This will allow you to use the functions choice explicitly
coin = random.choice(["heads", "tails"])
print(coin)

# using random.randint(a, b)
import random
number = random.randint(1, 10)
print(number)

#using random.shuffle(x)
import random
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)




