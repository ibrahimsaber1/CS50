import sys
import os

def line_count(file_name):
    count = 0
    try:
        with open(file_name , "r") as file:
            for line in file:
                strip_line = line.lstrip()
                if strip_line and not strip_line.startswith("#") and not strip_line.isspace():
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count


def main():
    #im checking the len of the argv first :-
    if len(sys.argv) != 2 :
        if len(sys.argv) < 2 :
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")


    if not os.path.isfile(file_name):
        sys.exit("File does not exist")

    count = line_count(file_name)
    print(count)

if __name__ == "__main__":
    main()
