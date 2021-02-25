# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd


RemaindersSideHeight = {}
def findMin():
    totalMin = min(RemaindersSideHeight)
    print(f"The combination of the least variance is: {RemaindersSideHeight.get(totalMin)}")


def drawGraph():

    # Create brown bars
    plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
    # Create green bars (middle), on top of the firs ones
    plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)

    # Custom X axis
    plt.xticks(r, names, fontweight='bold')
    plt.xlabel("Triangle Variance of Side and Height")

    # Show graphic
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #### GRAPH CALCULATION
    # y-axis in bold
    rc('font', weight='bold')

    # Values of each group
    bars1 = []
    bars2 = []

    # Names of group and bar width
    names = []
    barWidth = .5

    ######################

    # open and read the file after the appending:
    f = open("triangle_data.txt", "r")
    myLine = f.readlines()

    for i in myLine:
        Side_A = i.split(",")[0]
        Height_A = i.split(",")[1]
        names.append(str(f"Side A = {Side_A} | Height A = {Height_A}"))

        accuracy_side = float(i.split(",")[2])
        bars1.append(float(accuracy_side))

        accuracy_height = float(i.split(",")[3])
        bars2.append(float(accuracy_height))

        RemaindersSideHeight[float(accuracy_height + accuracy_side)] = str(f"Side A = {Side_A} | Height A = {Height_A}")

    findMin()
    #########################

    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()

    # The position of the bars on the x-axis
    r = []
    counter = int(0)
    for i in range(len(names)):
        r.append(counter)
        counter += 1

    drawGraph()
