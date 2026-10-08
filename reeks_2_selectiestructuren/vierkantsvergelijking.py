import math

a = float(input())
b = float(input())
c = float(input())

discriminant = pow(b, 2) - 4 * a * c

if (discriminant < 0):
    print("geen wortels")
elif (discriminant == 0):
    print("een wortel")
    wortel = -1 * (b / (2 * a))
    print(wortel)
else:
    print("twee wortels")
    wortel_1 = (-b - math.sqrt(discriminant)) / (2 * a)
    wortel_2 = (-b + math.sqrt(discriminant)) / (2 * a)

    if (wortel_1 > wortel_2):
        temp = wortel_2
        wortel_2 = wortel_1
        wortel_1 = temp

    print(wortel_1, wortel_2, sep="\n")
