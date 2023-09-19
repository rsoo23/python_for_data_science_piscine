
def ft_tqdm(lst: range) -> None:
    '''
    replicates the tqdm loading bar
    '''
    percentage = 0
    for n in lst:
        ratio = (n + 1) / (lst[-1] + 1)
        percentage = ratio * 100
        format_percentage = "{:>3.0f}".format(percentage)
        loading_bar = ""

        i = 0
        while i < ratio * 149:
            loading_bar += "█"
            i += 1
        format_loading_bar = "{:<149}".format(loading_bar)

        if n == lst[-1]:
            print(format_percentage + "%|", end="")
            print(format_loading_bar, end="")
            print("| " + str(n + 1) + "/" + str(lst[-1] + 1), end='\r')
            break

        print(format_percentage + "%|", end="")
        print(format_loading_bar, end="")
        print("| " + str(n + 1) + "/" + str(lst[-1] + 1), end='\r')
        yield percentage
