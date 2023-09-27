
class calculator:
    '''calculator class'''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''dot product between vectors'''
        total = 0.0
        prod = [(n1 * n2) for n1, n2 in zip(V1, V2)]
        for n in prod:
            total += n
        print("Dot product is: " + str(total))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''addition between vectors'''
        print("Add Vector is: " +
              str([float(n1 + n2) for n1, n2 in zip(V1, V2)]))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''subtraction between vectors'''
        print("Sous Vector is: " +
              str([float(n1 - n2) for n1, n2 in zip(V1, V2)]))
