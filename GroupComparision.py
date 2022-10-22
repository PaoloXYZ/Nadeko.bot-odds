import matplotlib.pyplot as plt
import random as r


def slot():
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

    
    attempts = 0
    betSize = 100
    initialAmount = 100000

    while True:#spins < 10000:
        if((initialAmount - betSize) < 0):
#           print("you can't afford the bet")
            break
        attempts += 1
        initialAmount -= betSize
        initialAmount += spin(betSize)

    return attempts 


# def wheel():
#     DEFAULT_MULTIPLIERS = [ 1.7, 1.5, 0.2, 0.1, 0.3, 0.5, 1.2, 2.4 ]
#     attempts = 0
#     initialAmount = 100000
#     betSize = 100


#     def spin(bet):
#         result = r.randint(0, 7)
#         multi = DEFAULT_MULTIPLIERS[result]
#         return bet * multi

#     while True:#attempts < 10000000:
#         if((initialAmount - betSize) < 0):
# #           print("you can't afford the bet")
#             break
#         attempts+=1
#         initialAmount -= betSize
#         initialAmount += spin(betSize)
#     return attempts


# def coinFlip():
#     DEFAULT_MULTIPLIER = 1.95
#     attempts = 0
#     initialAmount = 100000
#     betSize = 100


#     def flip(bet, guess):
#         result = r.randint(0, 1)
#         return bet * DEFAULT_MULTIPLIER if guess == result else 0


#     while True:#attempts < 10000000:
#         if((initialAmount - betSize) < 0):
# #           print("you can't afford the bet")
#             break
#         attempts+=1
#         initialAmount -= betSize
#         initialAmount += flip(betSize, r.randint(0, 1))
#     return attempts


# main
if __name__ == "__main__":
    nSim = 10000
    sumValueSlot = 0
    # sumValueFlips = 0
    # sumValueWheel = 0

    countSlots = 0
    # countFlips = 0
    # countWheel = 0

    xS = []
    yS = []

    # xF = []
    # yF = []


    # xW = []
    # yW = []

    slotV = 0
    # wheelV = 0
    # flipsV = 0

    while countSlots < nSim:
        countSlots += 1
        slotV = slot()
        xS.append(countSlots)
        yS.append(slotV)
        sumValueSlot += slotV
    plt.plot(xS, yS, label="Slots", color="green")

    # while countWheel< nSim:
    #     countWheel += 1
    #     wheelV = wheel()
    #     xW.append(countWheel)
    #     yW.append(wheelV)
    #     sumValueWheel += wheelV
    # plt.plot(xW, yW, label="Wheel Spins", color="red")

    # while countFlips < nSim:
    #     countFlips += 1
    #     flipsV = coinFlip()
    #     xF.append(countFlips)
    #     yF.append(flipsV)
    #     sumValueFlips += flipsV
    # plt.plot(xF, yF, label="Coinflips", color="blue")

    print("average Slot value: " , (sumValueSlot/nSim))
    # print("average Wheel value: " , (sumValueWheel/nSim))
    # print("average Coinflips value: ", (sumValueFlips/nSim))
    # plt.legend(["Slots", "Lucky Ladder", "Coinflips"])
    # plt.legend(["Lucky Ladder", "Coinflips"])
    # plt.show()
    plt.title("Slot Simulation")
    plt.xlabel("Count")
    plt.ylabel("Bet Number")
    # plt.plot(x,y)
    plt.savefig("plot1000-FullPlot.png")

