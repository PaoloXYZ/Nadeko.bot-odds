import matplotlib.pyplot as plt
import random as r
DEFAULT_MULTIPLIERS = [ 1.7, 1.5, 0.2, 0.1, 0.3, 0.5, 1.2, 2.4 ]
attempts = 0
initialAmount = 100000
betSize = 100
x = []
y = []


def spin(bet):
    result = r.randint(0, 7)
    multi = DEFAULT_MULTIPLIERS[result]
    return bet * multi

while True:#attempts < 10000000:
    if((initialAmount - betSize) < 0):
        # print("you can't afford the bet")
        break
    x.append(attempts)
    y.append(initialAmount)
    attempts+=1
    initialAmount -= betSize
    initialAmount += spin(betSize)

plt.title("Lucky Ladder Simulation")
plt.xlabel("Bet Number")
plt.ylabel("Credits")
plt.plot(x,y)
# plt.savefig("LuckyLadderSave.png")
plt.show()
