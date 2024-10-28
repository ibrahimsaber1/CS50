
def main():
    time = input("what time is it : ")
    meal_hour = convert(time)
    if 7 <= meal_hour <= 8:
        print("breakfast time")
    elif 12 <= meal_hour <= 13:
        print("lunch time")
    elif 18 <= meal_hour <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes/60


if __name__ == "__main__":
    main()
