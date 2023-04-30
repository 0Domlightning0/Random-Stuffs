
# Dominik Wrobel

# 2023 - Apr - 29



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
yes = True

while yes == True:
    Inputs = input("14 Black and white code ")

    if len(Inputs) >= 14 or Inputs == "C":
        print("Start")
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
            if i == 6:
                if Inputs[i] == "B":
                    Line3 += "-- "
                if Inputs[i] == "W":
                    Line3 += "   "

            # Line 4

            if i == 7:
                if Inputs[i] == "B":
                    Line4 += "|"
                if Inputs[i] == "W":
                    Line4 += " "
            if i == 8:
                if Inputs[i] == "B":
                    Line4 += "/"
                if Inputs[i] == "W":
                    Line4 += " "
            if i == 9:
                if Inputs[i] == "B":
                    Line4 += "|"
                if Inputs[i] == "W":
                    Line4 += " "
            if i == 10:
                if Inputs[i] == "B":
                    Line4 += "\\"
                if Inputs[i] == "W":
                    Line4 += " "
            if i == 11:
                if Inputs[i] == "B":
                    Line4 += "| "
                if Inputs[i] == "W":
                    Line4 += "  "

            # Line5


            if i == 12:
                Line5 += " "
                if Inputs[i] == "B":
                    Line5 += "---  "
                if Inputs[i] == "W":
                    Line5 += "     "
    else:
        print("Too short bro")

    print(Line1)
    print(Line2)
    print(Line3)
    print(Line4)
    print(Line5)

