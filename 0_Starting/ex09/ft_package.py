
def count_in_list(lst: list, string: str) -> int:
    '''
    count the number of the input string present in the list
    '''
    num_of_matches = 0

    for s in lst:
        if s == string:
            num_of_matches += 1
    return num_of_matches
