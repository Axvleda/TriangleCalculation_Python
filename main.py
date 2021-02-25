
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
import random
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'This is a Project for {name}')  # Press Strg+F8 to toggle the breakpoint.


def Triangle_Check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        # print(f'\bVALID TRIANGLE ~ ({a}, {b}, {c})')
        return True
    else:
        print(f'({a}, {b}, {c}) is not a valid triangle.')
        return False


def HeightOfSideATriangle(a, b, c):
    # sin(60) because of 60 ° angle meaning all sides are equal length
    degrees = 60 / 180 * math.pi
    height = b * math.sin(degrees)
    # print(f'Sidelength "A" is {a} | Height from Side "A" is {height}.')
    return height

def write2file(String):
    f = open("triangle_data.txt", "a")
    f.write(String)
    f.close()

# def Checker(remainder_height, remainder_side):
#     newHeight = min(remainder_height, float(1-remainder_height))
#     newSide = min(remainder_side, float(1-remainder_side))
#
#     print(f"height = {newHeight * newHeight} | side = {newSide * newSide}")

def Side_Check(remainder_side):
    Side = min(remainder_side, float(.5-remainder_side))
    sqSide = float(Side) * float(Side)
    newSide = float(math.sqrt(sqSide))
    return newSide

def Height_Check(remainder_height):
    Height = min(remainder_height, float(.5-remainder_height))
    # print(f"normal = {remainder_height} | extra = {float(1-remainder_height)}")
    sqHeight = float(Height) * float(Height)
    # print(f"sqHeight = {sqHeight}")
    newHeight = float(math.sqrt(sqHeight))
    # print(f"rootHeight = {newHeight}")
    return newHeight

def Check_HeightAndSides(treshold, myFloat):
    if Triangle_Check(myFloat, myFloat, myFloat):
        height = HeightOfSideATriangle(myFloat, myFloat, myFloat)

        remainder_height = height % .5
        remainder_side = myFloat % .5

        new_remainder_height = Height_Check(remainder_height)
        new_remainder_side = Side_Check(remainder_side)


        if new_remainder_height < treshold and new_remainder_side < treshold:
            print("\rpossible Solution found!")
            myString = f'Side A = %.3f | Height A = {height} | accuracy_side = {new_remainder_side} | accuracy_height = {new_remainder_height}' %myFloat
            sys.stdout.write("\b\r" + myString)
            sys.stdout.flush()

            String_Point = f"{myFloat}, {height}, {new_remainder_side}, {new_remainder_height}"
            write2file(String_Point + "\n")

            return True
        else:
            myString = f"Side A = %.3f | Not exact enough ({treshold}) ~ rem = {new_remainder_height} | {new_remainder_side} " %myFloat
            sys.stdout.write(myString + "\r")
            sys.stdout.flush()
            return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Triangle Calculation')

    while True:

        for i in range(300, 15000, 1): # given in millimeters


            i = i/100
            if Check_HeightAndSides(.01, i):

                print("\n")

        # open and read the file after the appending:
        f = open("triangle_data.txt", "r")
        myLine = f.read()
        print(f"The total length of worthy combinations is {len(myLine)}.")
        break










