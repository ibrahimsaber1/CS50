import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattren = r"\bum\b"
    matches = re.findall(pattren, s, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
