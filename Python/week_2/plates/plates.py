def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not (6 >= len(s) >= 2):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    n_start = False
    for char in s:
        if char.isdigit():
            if not n_start and char == '0':
                return False
            n_start = True
        elif n_start and char.isalpha():
            return False

    for char in s:
        if not char.isalnum():
            return False

    return True

main()
