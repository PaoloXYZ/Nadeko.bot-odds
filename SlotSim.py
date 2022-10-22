import matplotlib.pyplot as plt
import random as r


def spin(bet):
    b = r.randint(0, 5)
    a = r.randint(0, 5)
    c = r.randint(0, 5)
    multi = 0

    if a == b and b == c:
        if a == 5:
            multi = 30
        else:
            multi = 10
    elif a == 5 and (b == 5 or c == 5) or (b == 5 and c == 5):
        multi = 4
    elif a == 5 or b == 5 or c == 5:
        multi = 1
    return bet * multi


if __name__ == "__main__":
    x = []
    y = []
    spins = 0
    betSize = 100
    initialAmount = 100000

    while True:#spins < 10000:
        if((initialAmount - betSize) < 0):
#           print("you can't afford the bet")
            break
        spins += 1
        initialAmount -= betSize
        initialAmount += spin(betSize)
        x.append(spins)
        y.append(initialAmount)

    plt.title("Slots Simulation")
    plt.xlabel("Bet Number")
    plt.ylabel("Credits")
    plt.plot(x,y)
    # plt.savefig("SlotSave.png")
    plt.show()


#  public enum SlotWinType : byte
# {
#     None,         = 0
#     SingleJoker,  = 1
#     DoubleJoker,  = 2
#     TrippleNormal,= 3
#     TrippleJoker, = 4
# }

