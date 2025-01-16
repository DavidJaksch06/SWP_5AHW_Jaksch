class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps < 0:
            raise ValueError("PS muss eine nicht-negative Zahl sein.")
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition ist nur zwischen zwei Auto-Objekten erlaubt.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraktion ist nur zwischen zwei Auto-Objekten erlaubt.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplikation ist nur zwischen zwei Auto-Objekten erlaubt.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        raise TypeError("Vergleich ist nur zwischen zwei Auto-Objekten erlaubt.")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        raise TypeError("Vergleich ist nur zwischen zwei Auto-Objekten erlaubt.")

    def __len__(self):
        return int(self.ps)

    def __repr__(self):
        return f"Auto({self.ps} PS)"


if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)

    print(a1 + a2)

    print(a2 - a1)

    print(a1 * a2)

    print(a1 == a2)
    print(a1 < a2)
    print(a1 > a2)

    print(len(a1))
    print(len(a2))

    try:
        print(a1 + 10)
    except TypeError as e:
        print(e)

    try:
        print(a1 < 100)
    except TypeError as e:
        print(e)
