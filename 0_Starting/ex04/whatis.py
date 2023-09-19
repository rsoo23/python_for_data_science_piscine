
import sys

# sys.argv[0] = filename


def main():
    '''
    Input an integer and if it is even, print: "I'm Even.". If it
    is odd, print: "I'm Odd."
    '''
    num_args = len(sys.argv) - 1

    if num_args == 0:
        return

    try:
        assert num_args == 1, "more than one argument is provided"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return

    try:
        assert sys.argv[1].isdigit() or sys.argv[1][0] == '-', \
            "arguments is not an integer"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

# entry point of script
# - if the script is running directly it will execute main(),
# otherwise if this file is imported as a module, it will not run


if __name__ == "__main__":
    main()
