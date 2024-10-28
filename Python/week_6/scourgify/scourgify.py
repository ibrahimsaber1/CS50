import sys
import csv

def main():
    # Check that the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Open the input CSV file and prepare to read its contents
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            students = []

            # Process each row to split the name into first and last name
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})

        # Open the output CSV file and write the reformatted data
        with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
