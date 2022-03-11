class Balance:

    amount = None


balance_1 = Balance()
# balance_1.amount(5000)


class Person(Balance):

    first_name = None
    last_name = None
    number = None


jack = Person()
jack.first_name = "Jack"
jack.last_name = "barbaro"
jack.number = "909756434"
jack.amount = 5000

print(jack.first_name, jack.last_name, jack.number, jack.amount)