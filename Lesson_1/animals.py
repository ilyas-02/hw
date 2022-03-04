class Dog:

    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f"{self.animal}: {self.voiceText}\n")


dog = Dog("Dog", "gaf gaf")
dog.voice()


class Cat:
    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f"{self.animal}: {self.voiceText}\n")


cat = Cat("Cat", "miu miu")
cat.voice()


class Cov:
    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f"{self.animal}: {self.voiceText}\n")


cov = Cov("Cov", "muuu")
cov.voice()


class Bear:
    def __init__(self, animal, voiceText):
        self.animal = animal
        self.voiceText = voiceText

    def voice(self):
        print(f"{self.animal}: {self.voiceText}")


bear = Bear("Bear", "bear growl")
bear.voice()
