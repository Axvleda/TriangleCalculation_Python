
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

def random_Iterator():
    myInt = random.uniform(3.0, 10.0)
    # print(f'\rMy random side length to get checked is: {myInt}.')
    return myInt


def Check_HeightAndSides(treshold, myFloat):
    if Triangle_Check(myFloat, myFloat, myFloat):
        height = HeightOfSideATriangle(myFloat, myFloat, myFloat)

        remainder_height = height % 1
        remainder_side = myFloat % .5
        if remainder_height < treshold and remainder_side < treshold:
            print("\rpossible Solution found!")
            myString = f'Side A = %.3f | Height A = {height} | accuracy_side = {remainder_side} | accuracy_height = {remainder_height}' %myFloat
            sys.stdout.write("\b\r" + myString)
            sys.stdout.flush()

            return True
        else:
            myString = f"Side A = %.3f | Not exact enough ({treshold}) ~ rem = {remainder_height} | {remainder_side} " %myFloat
            sys.stdout.write(myString + "\r")
            sys.stdout.flush()
            return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Triangle Calculation')


# #Random Check
# while True:
#     if Check_HeightAndSides(.04):
#         break


while True:

    for i in range(300, 15000, 1): # given in millimeters


        i = i/100
        if Check_HeightAndSides(.05, i):

            print("\n")

    break








