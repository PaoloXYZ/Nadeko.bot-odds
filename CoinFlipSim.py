import matplotlib.pyplot as plt
import random as r

DEFAULT_MULTIPLIER = 1.95
attempts = 0
initialAmount = 100000
betSize = 100
x = []
y = []


def flip(bet, guess):
    result = r.randint(0, 1)
    return bet * DEFAULT_MULTIPLIER if guess == result else 0


while True:#attempts < 10000000:
    if((initialAmount - betSize) < 0):
        # print("you can't afford the bet")
        break
    x.append(attempts)
    y.append(initialAmount)
    attempts+=1
    initialAmount -= betSize
    initialAmount += flip(betSize, r.randint(0, 1))
    
plt.title("Coin Flip Simulation")
plt.xlabel("Bet Number")
plt.ylabel("Credits")
plt.plot(x,y)
# plt.savefig("CoinFlipSave.png")
plt.show()

