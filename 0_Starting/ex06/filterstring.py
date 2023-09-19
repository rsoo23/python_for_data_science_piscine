
import sys


# lambda
def check_len(min_len):
    '''
    checks the if the length of the string is longer than the minimum length
    '''
    return lambda str: len(str) > min_len


def main():
    '''
    takes in a string and minimum length and separates words delimited by
    spaces, placing them into a string. then it outputs a list that contains
    all the words that are longer than the minimum length
    '''
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return

    try:
        assert sys.argv[2].isdigit(), \
            "the second argument has to be an integer"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return

    input_str = sys.argv[1]
    min_length = int(sys.argv[2])

    word_list = input_str.split()

    check_length = check_len(min_length)

    # list comprehension
    new_list = [word for word in word_list if check_length(word)]

    print(new_list)


if __name__ == "__main__":
    main()
