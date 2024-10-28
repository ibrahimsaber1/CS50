def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date_input = input("Date: ").strip()

            # Check if input is in MM/DD/YYYY format
            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            # Check if input is in Month Day, Year format
            elif "," in date_input:
                month_day, year = date_input.split(", ")
                month_name, day = month_day.split(" ")
                day = int(day)
                year = int(year)

                if month_name in months and 1 <= day <= 31:
                    month = months.index(month_name) + 1
                    print(f"{year}-{month:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            pass

main()
