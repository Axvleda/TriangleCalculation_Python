import decimal
# Project will be continued to find best combination for area message

# TODO: Implement Area Message


import random
import math
import sys


# # def Checker(remainder_height, remainder_side):
# #     newHeight = min(remainder_height, float(1-remainder_height))
# #     newSide = min(remainder_side, float(1-remainder_side))
# #
# #     print(f"height = {newHeight * newHeight} | side = {newSide * newSide}")
#
# def Side_Check(remainder_side):
#     Side = min(remainder_side, float(.5-remainder_side))
#     sqSide = float(Side) * float(Side)
#     newSide = float(math.sqrt(sqSide))
#     return newSide
#
# def Height_Check(remainder_height):
#     Height = min(remainder_height, float(.5-remainder_height))
#     # print(f"normal = {remainder_height} | extra = {float(1-remainder_height)}")
#     sqHeight = float(Height) * float(Height)
#     # print(f"sqHeight = {sqHeight}")
#     newHeight = float(math.sqrt(sqHeight))
#     # print(f"rootHeight = {newHeight}")
#     return newHeight


# def Check_HeightAndSides(treshold, myFloat):
#     if Triangle_Check(myFloat, myFloat, myFloat):
#         height = HeightOfSideATriangle(myFloat, myFloat, myFloat)
#
#         remainder_height = height % .5
#         remainder_side = myFloat % .5
#
#         new_remainder_height = Height_Check(remainder_height)
#         new_remainder_side = Side_Check(remainder_side)
#
#
#         if new_remainder_height < treshold and new_remainder_side < treshold:
#             print("\rpossible Solution found!")
#             myString = f'Side A = %.3f | Height A = {height} | accuracy_side = {new_remainder_side} | accuracy_height = {new_remainder_height}' %myFloat
#             sys.stdout.write("\b\r" + myString)
#             sys.stdout.flush()
#
#             String_Point = f"{myFloat}, {height}, {new_remainder_side}, {new_remainder_height}"
#             write2file(String_Point + "\n")
#
#             return True
#         else:
#             myString = f"Side A = %.3f | Not exact enough ({treshold}) ~ rem = {new_remainder_height} | {new_remainder_side} " %myFloat
#             sys.stdout.write(myString + "\r")
#             sys.stdout.flush()
#             return False


# Todo: important Part Starts here!


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'This is a Project for {name}')  # Press Strg+F8 to toggle the breakpoint.


def write2file(String):
    f = open("triangle_data_sketch.txt", "a")
    f.write(String)
    f.close()


def Triangle_Check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        # print(f'\bVALID TRIANGLE ~ ({a}, {b}, {c})')
        return True
    else:
        print(f'({a}, {b}, {c}) is not a valid triangle.')
        return False


def Height_A(a):
    # sin(60) because of 60 ° angle meaning all sides are equal length
    degrees = 60 / 180 * math.pi
    height = a * math.sin(degrees)
    # print(f'Sidelength "A" is {a} | Height from Side "A" is {height}.')
    return height


def Area_A(side_a, height_a):
    area = float((side_a * height_a) / 2)
    return area


def Side_Height_Area(side_a):
    height = side_a * math.sin(((60 / 180) * math.pi))
    area = (side_a * height) / 2
    combination = [side_a, height, area]
    return combination


def quickstart(i, worthy_StellenAnzahl):
    side_a_StellenAnzahl = len(str(i))
    if (side_a_StellenAnzahl < worthy_StellenAnzahl):
        sys.stdout.write(f"{i} break")
        sys.stdout.flush()
        i = int(str(1) + (str(worthy_StellenAnzahl * "0"))) + 1
        return i


def reason_to_break(combination, worthy, i):
    #     if any of the numbers with dezimalstellen or ohne enthält WorthyCombination

    for comb in combination[2:]:

        combination_remainder = (comb % 1)
        worthy_StellenAnzahl = len(str(worthy))
        comb_beforeDecimal = str(comb).split(".")[0]
        comb_beforeDecimal_Stellen = len(str(comb_beforeDecimal))
        comb_afterDecimal = str((combination_remainder * (10 ** worthy_StellenAnzahl) + 1)).split(".")[0]
        comb_afterDecimal_Stellen = len(str(comb_afterDecimal))

        ## debug info
        # sys.stdout.write(
        #     f"\r\b\rStart:{i}. Side = {combination[0]}\t| Height = {combination[1]:8}\t| Area = {float(combination[2]):8}\t "
        #     f"| Worthy = {worthy}\t | Stellen: {worthy_StellenAnzahl} "
        #     f"\t Comb_beforeDecimal = {comb_beforeDecimal}\t | Stellen: {comb_beforeDecimal_Stellen}\t | "
        #     f"Comb_afterDecimal = {comb_afterDecimal}\t | Stellen: {comb_afterDecimal_Stellen}.")
        # sys.stdout.flush()

        # starte bei i größer als worthy
        # myint = int((str("1") + worthy_StellenAnzahl * str("0")))

        if (comb_afterDecimal) == str(worthy):
            sys.stdout.write(
                f"\rStart:{i}. Side = {combination[0]}\t| Height = {combination[1]:8}\t| Area = {float(combination[2]):8}\t "
                f"| Worthy = {worthy}\t | Stellen: {worthy_StellenAnzahl} "
                f"\t Comb_beforeDecimal = {comb_beforeDecimal}\t | Stellen: {comb_beforeDecimal_Stellen}\t | "
                f"Comb_afterDecimal = {comb_afterDecimal}\t | Stellen: {comb_afterDecimal_Stellen}.")

            return True

        elif (comb_beforeDecimal) == str(worthy):
            sys.stdout.write(
                f"\r\b\rStart:{i}. Side = {combination[0]}\t| Height = {combination[1]:8}\t| Area = {float(combination[2]):8}\t "
                f"| Worthy = {worthy}\t | Stellen: {worthy_StellenAnzahl} "
                f"\t Comb_beforeDecimal = {comb_beforeDecimal}\t | Stellen: {comb_beforeDecimal_Stellen}\t | "
                f"Comb_afterDecimal = {comb_afterDecimal}\t | Stellen: {comb_afterDecimal_Stellen}.")

            return True

        else:

            sys.stdout.write(f"\r {i}")
            sys.stdout.flush()
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Triangle Calculation')

WorthyCombinations = [703193977868615, 19940204, 19920813, 20201226]  # Test

# WorthyCombinations = [940204, 19920813, 20201226]

for i in range(1, sys.maxsize):

    for worthy in WorthyCombinations:
        # i = int(quickstart(i, len(str(worthy))))
        combination = Side_Height_Area(i)
        if (reason_to_break(combination, WorthyCombinations, i)):
            print("\n\nSuccess\n\n")
            break

# for i in range(1600):
#     combination = iter(Side_Height_Area(i))
#     if combination != 15:
#         combination.next()

# import itertools
# for i in itertools.count():
#     if reason_to_break(i):
#         height_a = Height_A(side_a)
#         area = Area_A(side_a, height_a)
#
#         sys.stdout.write(f"\rSide = {side_a} | Height = {height_a} | Area = {float(area)}")
#         sys.stdout.flush()

# while True:
#
#     for i in range(1, 15000, 1): # Boundaries g
#
#
#         i = i/100
#         if Check_HeightAndSides(.01, i):
#
#             print("\n")
#
#     # open and read the file after the appending:
#     f = open("triangle_data_sketch.txt", "r")
#     myLine = f.read()
#     print(f"The total length of worthy combinations is {len(myLine)}.")
#     break
