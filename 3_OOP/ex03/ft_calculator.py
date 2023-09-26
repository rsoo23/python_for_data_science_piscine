
class calculator:
    '''Calculator class'''
    def __init__(self, num_list) -> None:
        '''Calculator class constructor'''
        self.num_list = num_list

    def __add__(self, n) -> None:
        '''Addition'''
        print([(num + n)for num in self.num_list])

    def __mul__(self, n) -> None:
        '''Multiplication'''
        print([(num * n)for num in self.num_list])

    def __sub__(self, n) -> None:
        '''Subtraction'''
        print([(num - n)for num in self.num_list])

    def __truediv__(self, n) -> None:
        '''Division'''
        if n == 0:
            print("Error: division by 0")
            return
        print([(num / n)for num in self.num_list])
