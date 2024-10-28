

import sys
import os
from PIL import Image ,ImageOps


def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_extensions = ('.jpg', '.jpeg', '.png')

    if not (input_file.lower().endswith(valid_extensions)) and (output_file.lower().endswith(valid_extensions)):
        sys.exit("Invalid input or output format. Supported formats: .jpg, .jpeg, .png")

    input_extension = os.path.splitext(input_file)[1].lower()
    output_extension = os.path.splitext(output_file)[1].lower()
    if input_extension != output_extension:
        sys.exit("Input and output file extensions do not match")


    if not os.path.exists(input_file):
        sys.exit(f"Input file '{input_file}' does not exist")

    try:
        input_image = Image.open(input_file)
        shirt_image = Image.open("shirt.png")

        input_image = ImageOps.fit(input_image, shirt_image.size)

        input_image.paste(shirt_image, shirt_image)

        input_image.save(output_file)

    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
