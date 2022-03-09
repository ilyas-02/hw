"""
Тема: Основные принципы ООП

    1: Абстракция
    2: Наследование
    3: Полиморфизм
    4: Инкапсуляция
"""

""" Абстракция """


class Animal:

    def __init__(self, name, type, color, voiceText):
        self.name = name
        self.type = type
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(self.voiceText)


""" Наследование """


class Dog(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)


class Cat(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)


rex = Dog('Rex', 'Domestic', 'Blue', 'gaf gaf!')
rex.voice()

barsik = Cat('Barsik', 'Domestic', 'White-Black', 'myew myew!')
barsik.voice()


""" Полиморфизм """


class Horse(Animal):

    def __init__(self, name, type, color, voiceText, speed, weight):
        super().__init__(name, type, color, voiceText)
        self.speed = speed
        self.weight = weight

    """полиморфизм"""



    def voice(self):
        print(f"{self.name}: {self.voiceText}")


mustang = Horse('Mustang', 'Domestic', 'brown', 'kukariku', 30, 250)
mustang.voice()



