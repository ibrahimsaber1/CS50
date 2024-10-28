from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()

# print(fonts)


if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    if sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("invalid input")
else:
    sys.exit("invalid input")

figlet.setFont(font=font)
user_input = input("Input: ")

print(figlet.renderText(user_input))
