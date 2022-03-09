class Material:

    def __init__(self, gibkosty, prochnosty, informationText):
        self.gibkosty = gibkosty
        self.prochnosty = prochnosty
        self.informationText = informationText

    def text(self):
        print(self.informationText)


class Derevo(Material):

    def __init__(self, gibkosty, prochnosty, informationText):
        super().__init__(gibkosty, prochnosty, informationText)

    def information_material(self):
        print(f"{self.informationText} Drevesina")


class Subject(Derevo):

    def __init__(self, gibkosty, prochnosty, informationText):
        super().__init__(gibkosty, prochnosty, informationText)

    def information(self):
        print(f"{self.informationText} stul, stol")
