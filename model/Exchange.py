class Exchange:
    def __init__(self, name, end_point):
        self._amount = 0
        self.name = name
        self.end_point = end_point

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
        pass

    @property
    def end_point(self):
        return self.end_point

    @end_point.setter
    def end_point(self, value):
        self._end_point = value

    def to_json(self):
        return {"name": self.name, "amount": self.amount,}
