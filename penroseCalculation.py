import math


def AreaCalculationTriangle(Side_A, Height_A):
    return float(Side_A * Height_A) / 2



def PenroseCoordinates(Side_A, Height_A):
    BaseTriangle_a = (0, 0)
    BaseTriangle_b = (Side_A, 0)
    BaseTriangle_c = (float(Side_A/2), Height_A)
    # Hypotenuse = Side_A #not relevant for 60° angles
    Coordinates  = [BaseTriangle_a, BaseTriangle_b, BaseTriangle_c]


    print(f"Side = {Side_A} | Height = {Height_A}. \t Coordinates = {Coordinates}. \n"
          f"Area of Triangle = {AreaCalculationTriangle( Side_A, Height_A)}")


def AreaCalculationGoofy(Side_A_inCentimetre, optional_arg1 = "1" , optional_arg2 = "2" ):

    if optional_arg1 == "1":
        VolumeinCm = Side_A_inCentimetre ** 3

    elif optional_arg2 == "2":
        VolumeinCm = Side_A_inCentimetre * optional_arg1 * 1

    else:
        VolumeinCm = Side_A_inCentimetre * optional_arg1 * optional_arg2


    Litre = VolumeinCm/1000
    Millilitre = Litre * 1000
    WeightinKG = Litre
    print(f"Side A = {Side_A_inCentimetre:,} centimetre | {Side_A_inCentimetre / 100:,} meters | {Side_A_inCentimetre / 10000:,} kilometers. \n"
          f"The occupy Volume: {VolumeinCm / 1000:,} m^3 | {Litre:,} litre | {Millilitre:,} ml Water at 4°. \n"
          f"Weight: { WeightinKG * 1000:,} g | {WeightinKG:,} kg | {WeightinKG/1000:,} t. \n")

if __name__ == "__main__":
    PenroseCoordinates(15, 12.990381056766578)

    # AreaCalculationGoofy(100)
    # AreaCalculationGoofy(10000, 10000, 10000)
    # AreaCalculationGoofy(100,10000, 1)
