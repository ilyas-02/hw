class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def start(self):
        print(f"{self.first_name} {self.last_name}")


class Jack(Person):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

    def none(self):
        pass


jack = Jack("Jack", "Jeckerson", 707647358, 100)


class Vito(Jack):
    _curren_balance = 10

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def _get_curren_balance(self):
        print(f"{self.first_name} {self.phone_number} balance {self._curren_balance}")

    def none(self):
        vito = jack.balance - self._curren_balance
        f = self.balance + vito
        print(f)


jack.none()

vito = Vito("Vito", "Vitonson", 998654276, 90)
vito.none()
