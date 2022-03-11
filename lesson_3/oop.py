class Buildeer:

    def can_build(self):
        print("i cea build!")


class Doctor:

    def can_help(self):
        print("i cea help!")


class Programmer:

    def cen_write_code(self):
        print("i cen write code!")

    def can_buiid(self):
        print("I am a programmer but i cen build!")


class Person(Buildeer, Doctor, Programmer):
    pass

jack = Person()
# print(Person.__mro__)
# jack.cen_write_code()

