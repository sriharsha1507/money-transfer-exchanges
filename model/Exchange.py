class Exchange:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @property
    def name(self):
        return self.name()

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    def to_json(self):
        return {"name": self.name, "amount": self.amount}