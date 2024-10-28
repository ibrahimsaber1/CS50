

def main():
    plate = input("Input: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 > len(s) or len(s) > 6:
        return False


    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    num_start = False

    for i in range(len(s)):
        #to check if any str are founsd after the integer :-
        if s[i].isalpha():
            if num_start :
                return False
            else:
                continue
        elif s[i].isdigit():
            if not num_start :
                if s[i] == '0':
                    return False
                num_start = True
            continue
        else :
            return False

    return True




if __name__ == "__main__":
    main()
