class Fraction:

    def __init__(self, numertor, denumerator):
        self.numbertor = numertor
        self.denumerator = denumerator

    def __add__(self, other):
        self.numbertor += other
        self.denumerator += other
        print(f"{self.numbertor}/{self.denumerator}")

        return self.numbertor, self.denumerator


    def __sub__(self, other):
        self.numbertor -= other
        self.denumerator -= other
        print(f"{self.numbertor}/{self.denumerator}")

        return self.numbertor, self.denumerator

    def __mul__(self, other):
        self.numbertor *= other
        self.denumerator *= other
        print(f"{self.numbertor}/{self.denumerator}")

        return self.numbertor, self.denumerator

    def __floordiv__(self, other):
        self.numbertor //= other
        self.denumerator //= other
        print(f"{self.numbertor}/{self.denumerator}")
        return self.numbertor, self.denumerator






num = Fraction(5, 10)
num + 6
num - 6
num * 6
num // 7

