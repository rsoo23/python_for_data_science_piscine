
import sys


def main():
    '''
    outputs the input string (alphanumeric characters and space) as morse code
    '''
    NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-",
        "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-",
        "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/ "
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return

    for char in sys.argv[1].upper():
        try:
            assert char in NESTED_MORSE, "the arguments are bad"
        except AssertionError as msg:
            print("Assertion Error: " + str(msg))
            return

    i = 0

    for char in sys.argv[1].upper():
        if i == len(sys.argv[1]) - 1:
            print(NESTED_MORSE[char])
            break
        i += 1
        print(NESTED_MORSE[char], end=" ")


if __name__ == "__main__":
    main()
