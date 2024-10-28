import csv
import random
import re
from datetime import datetime
from countries import get_country_list

# ---------------------------------------------------------------------
# List of disallowed countries for DV Lottery
DISALLOWED_COUNTRIES = [
    "China", "India", "Mexico", "Philippines", "Nigeria", "Pakistan",
    "Bangladesh", "Russia", "Vietnam", "Ukraine"
]
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# List of allowed education levels
EDUCATION_LEVELS = [
    "None",
    "Primary School",
    "Elementary School",
    "High School",
    "Bachelor Degree",
    "Master",
    "PhD"
]

VALID_EDUCATION_LEVELS = [
    "High School",
    "Bachelor Degree",
    "Master",
    "PhD"
]

VALID_ENTRIES_FILE = "dv_valid_entries.csv"
INVALID_ENTRIES_FILE = "dv_invalid_entries.csv"
# ---------------------------------------------------------------------



# --------------------- Main Function -----------------------------------
def main():
    """Main function to execute the DV Lottery application process."""
    while True:
        print("\nChoose an option:")
        print("*" * 50)
        print("1. Submit a DV Lottery Application")
        print("2. Select a Random Winner")
        print("3. Exit")
        print("*" * 50)

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            application = get_user_input()
            is_valid, errors = validate_application(application)
            if is_valid:
                store_application(application, is_valid=True)
                print()
                print("*" * 50)
                print("Your application has been submitted and is valid :)")
            else:
                store_application(application, is_valid=False)
                print()
                print("*" * 50)
                print("Your application is invalid for the following reasons:")
                for error in errors:
                    print(f"- {error}")
        elif choice == '2':
            winner = select_random_winner()
            if winner:
                print()
                print("*" * 50)
                print("\n=== Random Winner ===")
                for key, value in winner.items():
                    print(f"{key}: {value}")
        elif choice == '3':
            print("*" * 50)
            print()
            print("See you soon :)")
            print("Exiting the program. Goodbye!")
            print("*" * 50)
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# --------------------(1)- Input Data Function ------------------------
def get_user_input():
    """Prompts the user to input their application details."""
    print("=== DV Lottery Application ===")
    print("*" * 50)

    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    middle_name = input("Middle Name: ").strip()
    date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()
    city_of_birth = input("City of Birth: ").strip()

    # Countries selection
    countries = get_country_list()
    print("\nSelect your Nationality from the list below by entering the corresponding number:")
    for num, country in enumerate(countries, 1):
        print(f"{num}. {country}")
    while True:
        try:
            country_choice = int(input("Enter the number corresponding to your country: "))
            if 1 <= country_choice <= len(countries):
                nationality = countries[country_choice - 1]
                break
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    address = input("Address (Optional): ").strip()
    email = input("Email (Optional): ").strip()
    phone_number = input("Phone Number (Optional): ").strip()

    # Education selection
    print("\nSelect your Education Level from the list below by entering the corresponding number:")
    for num, edu in enumerate(EDUCATION_LEVELS, 1):
        print(f"{num}. {edu}")
    while True:
        try:
            edu_choice = int(input("Enter the number corresponding to your education level: "))
            if 1 <= edu_choice <= len(EDUCATION_LEVELS):
                education = EDUCATION_LEVELS[edu_choice - 1]
                break
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    application = {
        "First Name": first_name,
        "Last Name": last_name,
        "Middle Name": middle_name,
        "Date of Birth": date_of_birth,
        "City of Birth": city_of_birth,
        "Nationality": nationality,
        "Address": address,
        "Email": email,
        "Phone Number": phone_number,
        "Education": education
    }

    return application

# --------------------(2)- Validation Function -------------------------
def validate_application(application):
    """Validates the application based on DV Lottery requirements."""
    errors = []

    # Check mandatory fields
    mandatory_fields = ["First Name", "Last Name", "Date of Birth", "City of Birth", "Nationality", "Education"]
    for field in mandatory_fields:
        if not application[field]:
            errors.append(f"{field} is required.")

    # Validate age (must be at least 18)
    try:
        dob = datetime.strptime(application["Date of Birth"], "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            errors.append("Applicant must be at least 18 years old.")
    except ValueError:
        errors.append("Date of Birth must be in YYYY-MM-DD format.")

    # Check nationality
    if application["Nationality"] in DISALLOWED_COUNTRIES:
        errors.append(f"Nationality '{application['Nationality']}' is not allowed to apply for the DV Lottery.")

    # Check education level
    if application["Education"] not in VALID_EDUCATION_LEVELS:
        errors.append("Education level must be at least High School.")

    # Optional: Validate email format if provided
    if application["Email"]:
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, application["Email"]):
            errors.append("Invalid email format.")

    # Optional: Validate phone number format if provided
    if application["Phone Number"]:
        phone_regex = r"^\+?1?\d{9,15}$"
        if not re.match(phone_regex, application["Phone Number"]):
            errors.append("Invalid phone number format.")

    is_valid = len(errors) == 0
    return is_valid, errors

# -------------------(3)-- Store Data Function ---------------------------
def store_application(application, is_valid, valid_file=VALID_ENTRIES_FILE, invalid_file=INVALID_ENTRIES_FILE):
    """Stores the application in the appropriate CSV file based on its validity."""
    filename = valid_file if is_valid else invalid_file
    fieldnames = list(application.keys())

    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write header only if file is empty
        csvfile.seek(0, 2)  # Move to end of file
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(application)

# -------------------(4)-- Winner Select Function ------------------------
def select_random_winner(valid_file=VALID_ENTRIES_FILE):
    """Selects a random winner from the valid entries."""
    try:
        with open(valid_file, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            entries = list(reader)
            if not entries:
                print("No valid entries available to select a winner.")
                return None
            winner = random.choice(entries)
            return winner
    except FileNotFoundError:
        print(f"The file '{valid_file}' does not exist.")
        return None



if __name__ == "__main__":
    main()
