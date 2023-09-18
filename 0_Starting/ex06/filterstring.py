
import sys

# lambda
check_len = lambda str, min_len: len(str) > min_len

def main():
    assert len(sys.argv) == 3, "the arguments are bad"

    assert sys.argv[2].isdigit(), "the second argument has to be an integer"

    input_str = sys.argv[1]
    min_length = int(sys.argv[2])

    word_list = input_str.split()

    # list comprehension
    new_list = [word for word in word_list if check_len(word, min_length)]

    print(new_list);

if __name__ == "__main__":
	main()
