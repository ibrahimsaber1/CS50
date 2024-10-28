expression = input("expression :")
x, y, z = expression.split(" ")
# print(x, y, z)
x = float(x)
z = float(z)

if y == "+":
    print(x + z ,end="")
elif y == "-":
    print(x - z ,end="")
elif y == "/":
    print(x / z ,end="")
elif y == "*":
    print(x * z ,end="")


