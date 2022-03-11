class Fraction:

    def __init__(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denomerator)

    def __add__(self, other):
        newnumerator = self.numerator * other.denomerator + self.denomerator * other.numerator
        newdenomerator = self.denomerator * other.denomerator
        return Fraction(newnumerator, newdenomerator)

    def __sub__(self, other):
        newnumerator = self.numerator * other.denomerator - self.denomerator * other.numerator
        newdenomerator = self.denomerator * other.denomerator
        return Fraction(newnumerator, newdenomerator)

    def __mul__(self, other):
        newnumerator = self.numerator * other.denomerator * self.denomerator * other.numerator
        newdenomerator = self.denomerator * other.denomerator
        return Fraction(newnumerator, newdenomerator)

    def __floordiv__(self, other):
        newnumerator = self.numerator * other.denomerator // self.denomerator * other.numerator
        newdenomerator = self.denomerator * other.denomerator
        return Fraction(newnumerator, newdenomerator)


n = Fraction(1, 4)
d = Fraction(1, 2)

print(n + d)
print(n - d)
print(n * d)
print(n // d)
