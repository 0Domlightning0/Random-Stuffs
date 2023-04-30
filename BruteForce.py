
# Dominik Wrobel

# 2023 - Apr - 29

# With double the rows!!!!!!

# B = Lit W = Not lit C = Next row



row = 1

print(" ___")
print("|\|/|")
print("-- --")
print("|/|\|")
print(" ---")
Line1 = ""
Line2 = ""
Line3 = ""
Line4 = ""
Line5 = ""
Line6 = ""
Line7 = ""
Line8 = ""
Line9 = ""
Line10 = ""
Line11 = ""
Line12 = ""
Line13 = ""
Line14 = ""
Line15 = ""
yes = True

A = "BBWWWBBBBWWWBW"
B = "BWWBWBWBWWBWBB"
C = "BBWWWWWWBWWWWB"

while yes == True:

    Inputs = input("14 Black and white code ")

    if Inputs == "C":
        row += 1


    if row == 1:
        if len(Inputs) >= 14 and Inputs != "C":
            for i in range(15):
                if i == 0:
                    Line1 += " "
                    if Inputs[i] == "B":
                        Line1 += "___  "
                    if Inputs[i] == "W":
                        Line1 += "     "


                # Line 2

                if i == 1:
                    if Inputs[i] == "B":
                        Line2 += "|"
                    if Inputs[i] == "W":
                        Line2 += " "
                if i == 2:
                    if Inputs[i] == "B":
                        Line2 += "\\"
                    if Inputs[i] == "W":
                        Line2 += " "
                if i == 3:
                    if Inputs[i] == "B":
                        Line2 += "|"
                    if Inputs[i] == "W":
                        Line2 += " "
                if i == 4:
                    if Inputs[i] == "B":
                        Line2 += "/"
                    if Inputs[i] == "W":
                        Line2 += " "
                if i == 5:
                    if Inputs[i] == "B":
                        Line2 += "| "
                    if Inputs[i] == "W":
                        Line2 += "  "

                # Line 3

                if i == 6:
                    if Inputs[i] == "B":
                        Line3 += "-- "
                    if Inputs[i] == "W":
                        Line3 += "   "
                if i == 7:
                    if Inputs[i] == "B":
                        Line3 += "-- "
                    if Inputs[i] == "W":
                        Line3 += "   "

                # Line 4

                if i == 8:
                    if Inputs[i] == "B":
                        Line4 += "|"
                    if Inputs[i] == "W":
                        Line4 += " "
                if i == 9:
                    if Inputs[i] == "B":
                        Line4 += "/"
                    if Inputs[i] == "W":
                        Line4 += " "
                if i == 10:
                    if Inputs[i] == "B":
                        Line4 += "|"
                    if Inputs[i] == "W":
                        Line4 += " "
                if i == 11:
                    if Inputs[i] == "B":
                        Line4 += "\\"
                    if Inputs[i] == "W":
                        Line4 += " "
                if i == 12:
                    if Inputs[i] == "B":
                        Line4 += "| "
                    if Inputs[i] == "W":
                        Line4 += "  "

                # Line5


                if i == 13:
                    Line5 += " "
                    if Inputs[i] == "B":
                        Line5 += "---  "
                    if Inputs[i] == "W":
                        Line5 += "     "

    if row == 2:
        if len(Inputs) >= 14 and Inputs != "C":
            for i in range(15):
                if i == 0:
                    Line6 += " "
                    if Inputs[i] == "B":
                        Line6 += "___  "
                    if Inputs[i] == "W":
                        Line6 += "     "

                # Line 2

                if i == 1:
                    if Inputs[i] == "B":
                        Line7 += "|"
                    if Inputs[i] == "W":
                        Line7 += " "
                if i == 2:
                    if Inputs[i] == "B":
                        Line7 += "\\"
                    if Inputs[i] == "W":
                        Line7 += " "
                if i == 3:
                    if Inputs[i] == "B":
                        Line7 += "|"
                    if Inputs[i] == "W":
                        Line7 += " "
                if i == 4:
                    if Inputs[i] == "B":
                        Line7 += "/"
                    if Inputs[i] == "W":
                        Line7 += " "
                if i == 5:
                    if Inputs[i] == "B":
                        Line7 += "| "
                    if Inputs[i] == "W":
                        Line7 += "  "

                # Line 3

                if i == 6:
                    if Inputs[i] == "B":
                        Line8 += "-- "
                    if Inputs[i] == "W":
                        Line8 += "   "
                if i == 7:
                    if Inputs[i] == "B":
                        Line8 += "-- "
                    if Inputs[i] == "W":
                        Line8 += "   "

                # Line 4

                if i == 8:
                    if Inputs[i] == "B":
                        Line9 += "|"
                    if Inputs[i] == "W":
                        Line9 += " "
                if i == 9:
                    if Inputs[i] == "B":
                        Line9 += "/"
                    if Inputs[i] == "W":
                        Line9 += " "
                if i == 10:
                    if Inputs[i] == "B":
                        Line9 += "|"
                    if Inputs[i] == "W":
                        Line9 += " "
                if i == 11:
                    if Inputs[i] == "B":
                        Line9 += "\\"
                    if Inputs[i] == "W":
                        Line9 += " "
                if i == 12:
                    if Inputs[i] == "B":
                        Line9 += "| "
                    if Inputs[i] == "W":
                        Line9 += "  "

                # Line10

                if i == 13:
                    Line10 += " "
                    if Inputs[i] == "B":
                        Line10 += "---  "
                    if Inputs[i] == "W":
                        Line10 += "     "

    if row == 3:
        if len(Inputs) >= 14 and Inputs != "C":
            for i in range(15):
                if i == 0:
                    Line11 += " "
                    if Inputs[i] == "B":
                        Line11 += "___  "
                    if Inputs[i] == "W":
                        Line11 += "     "

                # Line 2

                if i == 1:
                    if Inputs[i] == "B":
                        Line12 += "|"
                    if Inputs[i] == "W":
                        Line12 += " "
                if i == 2:
                    if Inputs[i] == "B":
                        Line12 += "\\"
                    if Inputs[i] == "W":
                        Line12 += " "
                if i == 3:
                    if Inputs[i] == "B":
                        Line12 += "|"
                    if Inputs[i] == "W":
                        Line12 += " "
                if i == 4:
                    if Inputs[i] == "B":
                        Line12 += "/"
                    if Inputs[i] == "W":
                        Line12 += " "
                if i == 5:
                    if Inputs[i] == "B":
                        Line12 += "| "
                    if Inputs[i] == "W":
                        Line12 += "  "

                # Line 3

                if i == 6:
                    if Inputs[i] == "B":
                        Line13 += "-- "
                    if Inputs[i] == "W":
                        Line13 += "   "
                if i == 7:
                    if Inputs[i] == "B":
                        Line13 += "-- "
                    if Inputs[i] == "W":
                        Line13 += "   "

                # Line 4

                if i == 8:
                    if Inputs[i] == "B":
                        Line14 += "|"
                    if Inputs[i] == "W":
                        Line14 += " "
                if i == 9:
                    if Inputs[i] == "B":
                        Line14 += "/"
                    if Inputs[i] == "W":
                        Line14 += " "
                if i == 10:
                    if Inputs[i] == "B":
                        Line14 += "|"
                    if Inputs[i] == "W":
                        Line14 += " "
                if i == 11:
                    if Inputs[i] == "B":
                        Line14 += "\\"
                    if Inputs[i] == "W":
                        Line14 += " "
                if i == 12:
                    if Inputs[i] == "B":
                        Line14 += "| "
                    if Inputs[i] == "W":
                        Line14 += "  "

                # Line15

                if i == 13:
                    Line15 += " "
                    if Inputs[i] == "B":
                        Line15 += "---  "
                    if Inputs[i] == "W":
                        Line15 += "     "

    if row == 1:
        print(Line1)
        print(Line2)
        print(Line3)
        print(Line4)
        print(Line5)

    if row == 2:

        print(Line1)
        print(Line2)
        print(Line3)
        print(Line4)
        print(Line5)
        print(Line6)
        print(Line7)
        print(Line8)
        print(Line9)
        print(Line10)

    if row == 3:
        print(Line1)
        print(Line2)
        print(Line3)
        print(Line4)
        print(Line5)
        print(Line6)
        print(Line7)
        print(Line8)
        print(Line9)
        print(Line10)
        print(Line11)
        print(Line12)
        print(Line13)
        print(Line14)
        print(Line15)

