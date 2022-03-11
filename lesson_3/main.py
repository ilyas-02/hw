class Balance:

    def __init__(self, num, username):
        self.num = num
        self.username = username
        
    def __str__(self):
        return f"{self.username}, balance {self.num}"

    def __add__(self, other):
        print("magic method __add__")
        self.num += other
        return self.num

    def __sub__(self, other):
        print("magic method __sub__")
        self.num -= other
        return self.num

    def __mul__(self, other):
        print("magic method __mul__")
        self.num *= other
        return self.num

    def __floordiv__(self, other):
        previous_num = self.num
        self.num //= other
        return f"{previous_num} // {other} = {self.num}"


jack_balance = Balance(5000, "Jack")
vito_balance = Balance(1000, "Vito")

print(jack_balance)
print(jack_balance // 2)

# print(jack_balance)








