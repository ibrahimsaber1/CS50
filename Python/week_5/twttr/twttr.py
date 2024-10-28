

def main():
    str1 = input("Input: ")
    print(shorten(str1))

def shorten(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''
    for char in word:
        if char.lower() not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
