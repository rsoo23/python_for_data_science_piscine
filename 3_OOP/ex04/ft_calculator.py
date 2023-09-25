class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        total = 0.0
        prod = [(n1 * n2) for n1, n2 in zip(V1, V2)]
        for n in prod:
            total += n
        print("Dot product is: " + str(total))

    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add Vector is: " +
              str([float(n1 + n2) for n1, n2 in zip(V1, V2)]))

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous Vector is: " +
              str([float(n1 - n2) for n1, n2 in zip(V1, V2)]))
