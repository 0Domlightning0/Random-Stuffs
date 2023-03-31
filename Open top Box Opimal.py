x = 0

y = float(input("Width "))

z = float(input("Legnth "))

Area = 0



FinalArea = 0

yes = 0

FinalX = 0

FinalArea = x * (y - (2 * x)) * (z - (2 * x))


while yes < 100000:

    if 2 * x < y-0.1 and 2 * x < z-0.1:

        Area = x * (y - (2 * x)) * (z - (2 * x))

        if FinalArea < Area:
            FinalArea = Area
            FinalX = x


        x += 0.001

        yes += 1


    if 2 * x >= y-0.1 or 2 * x >= z-0.1:
        yes = 10000000000000000


print(FinalArea)

print(FinalX)

print(y/FinalX)