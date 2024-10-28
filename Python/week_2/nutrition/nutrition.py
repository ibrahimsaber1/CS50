fruits= {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "blueberries": 85,
    "grapes": 90,
    "kiwifruit": 90,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "strawberries": 50,
    "sweet cherries": 100,
    "watermelon": 80
}

f_name = input("Item: ").strip().lower()

if f_name in fruits :
    print(f"Calories: {fruits[f_name]}")
