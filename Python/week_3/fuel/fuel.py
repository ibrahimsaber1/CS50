while True:
    try:
        fule_amount = input("fractions: ").strip()
        fule_amount = fule_amount.split("/")

        if len(fule_amount) != 2:
            raise ValueError("Invalid input format")

        if int(fule_amount[1]) == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if int(fule_amount[0]) > int(fule_amount[1]):
            raise ValueError("Numerator cannot be greater than denominator")

        fule_fractions = int(fule_amount[0]) / int(fule_amount[1])
        fule_fractions = round(fule_fractions * 100)

        if fule_fractions >= 99:
            print("F")
            break
        elif fule_fractions <= 1:
            print("E")
            break
        else:
            print(f"{fule_fractions}%")
            break

    except (ValueError, ZeroDivisionError):
        pass
