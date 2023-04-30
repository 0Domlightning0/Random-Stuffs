# 2023

# With 1 row!!!!!!

# Giving you 14 digit codes since 2005!!!!

# B = Lit W = Not lit

Chaarcter = input("Read the comments,What character? ")

# Add a space for blank and any text for lit

Line1 = input("Line1 ")
Line2 = input("Line2 ")
Line3 = input("Line3 ")
Line4 = input("Line4 ")
Line5 = input("Line5 ")

Code = ""


if Line1 == "":
    Code += "W"
else:
    Code += "B"
for i in range(5):
    if Line2[i] == " ":
        Code += "W"
    else:
        Code += "B"
for i in range(2):
    if Line3[i] == " ":
        Code += "W"
    else:
        Code += "B"
for i in range(5):
    if Line4[i] == " ":
        Code += "W"
    else:
        Code += "B"
if Line5 == "":
    Code += "W"
else:
    Code += "B"

print(Code)

print(Chaarcter + " = " + "'" + Code + "'")
