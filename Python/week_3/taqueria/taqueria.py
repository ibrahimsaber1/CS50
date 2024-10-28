menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

count = 0
while True:
    try:
        item = input("item: ").strip().title()
        if item not in menu :
            raise ValueError("This item not in the menu")
        else:
            count = count + menu[item]
            print(f"${count:.2f}")
    except EOFError:
        break
    except ValueError:
        pass
