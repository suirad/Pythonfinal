"Implements Question 1"
import math

rad = int(input("Please give Radius: "))

print(
    "diameter: {}\ncircumference: {}\narea: {}".format(
        2*rad,
        2 * math.pi * rad,
        math.pi*(rad*rad)
    )
)