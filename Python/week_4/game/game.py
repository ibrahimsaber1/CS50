import random


while True:
    try:
        num1 = int(input("Level: "))
        break
    except:
        pass
num2 = random.randint(0,num1)

while True:
    while True:
        try:
            num3 = int(input("Guess: "))
            break
        except:
            pass
    if num3 < num2 :
        print("Too small!")
        continue
    elif num3 > num2:
        print("Too large!")
        continue
    else:
        print("Just right!",end="")
        break
