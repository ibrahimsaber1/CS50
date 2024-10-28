import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            table = list(reader)

            if not table:
                sys.exit("The CSV file is empty")

            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
