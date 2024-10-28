def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
            output = gauge(percentage)
            print(output)
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    numerator, denominator = fraction.split('/')

    numerator = int(numerator)
    denominator = int(denominator)

    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    if numerator > denominator:
        raise ValueError("Numerator cannot be greater than denominator")

    percentage = round((numerator / denominator) * 100)
    return percentage

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
