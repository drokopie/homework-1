import math
paintColors = {
    'red': 35,
    'blue': 25,
    'green':23
}

wallHeight = float(input("Enter wall height (feet):\n"))
wallWidth = float(input("Enter wall width (feet):\n"))
area = wallHeight*wallWidth
print("Wall area: {:.0f} square feet".format(area))
paintNeeded = area/350
print("Paint needed: {:.2f} gallons".format(paintNeeded))
print("Cans needed: {} can(s)".format(math.ceil(paintNeeded)))
color = input("\nChoose a color to paint the wall:\n")
print("Cost of purchasing {} paint: $".format(color),end="")
print(paintColors[color])