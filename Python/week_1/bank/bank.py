greating = input("Greating: ").lower().strip()

if greating[0:5] == "hello":
    print("$0")
elif greating[0] == "h" and greating[0:5] != "hello":
    print("$20")
else:
    print("$100")



