import re



def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattren = r"(\d{1,2}(:\d{2})?) ?(AM|PM) to (\d{1,2}(:\d{2})?) ?(AM|PM)"
    match = re.match(pattren , s)


    start_time, _, start_period, end_time, _, end_period = match.groups()
    start_24 = convert_to_24_hour(start_time, start_period)
    end_24 = convert_to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"

def convert_to_24_hour(time, period):
    if ":" in time:
        hour, minute = time.split(":")
    else:
        hour, minute = time, "00"

    hour = int(hour)
    minute = int(minute)

    if not (0 <= hour <= 12 and 0 <= minute < 60):
        raise ValueError("Invalid time")

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
