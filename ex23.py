import sys
script, input_encoding, error = sys.argv


# define the main function that takes in 3 arguments
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        # call the print_line function
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# function to print the encoded line (in byte) and the decoded line
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
