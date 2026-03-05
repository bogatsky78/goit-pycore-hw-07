class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        return str(self.value)
