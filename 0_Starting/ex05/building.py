
import sys
import string


def main():
    '''
    Takes a string as an argument, outputs the number of uppercase, lowercase,
    punctuation marks, spaces, and digits. If nothing is input, the program
    will prompt the user to enter a string.
    '''
    num_args = len(sys.argv) - 1
    num_up = 0
    num_low = 0
    num_punc = 0
    num_spaces = 0
    num_digit = 0

    try:
        assert num_args == 1 or num_args == 0, \
            "more than one argument is provided"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return

    if num_args == 0:
        input_str = input("What is the text to count?\n")
    else:
        input_str = sys.argv[1]

    for char in input_str:
        if char.isupper():
            num_up += 1
        elif char.islower():
            num_low += 1
        elif char in string.punctuation:
            num_punc += 1
        elif char.isspace():
            num_spaces += 1
        elif char.isdigit():
            num_digit += 1

    print("The text contains " + str(len(input_str)) + " characters:")
    print(str(num_up) + " upper letters")
    print(str(num_low) + " lower letters")
    print(str(num_punc) + " punctuation marks")
    print(str(num_spaces) + " spaces")
    print(str(num_digit) + " digits")


if __name__ == "__main__":
    main()
