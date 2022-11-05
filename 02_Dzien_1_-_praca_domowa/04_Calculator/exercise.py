class Calculator:
    def add(self, a, b):
        self.add = a + b
        return self.add

    def sub(self, a, b):
        self.sub = a - b
        return self.sub

    def mul(self, a, b):
        self.mul = a * b
        return self.mul

    def div(self, a, b):
        self.div = a / b
        return self.div


class LoggingCalculator(Calculator):
    history = []

    def add(self, a, b):
        super().add(a, b)
        LoggingCalculator.history.append(f'{a}+{b}={self.add}')
        return self.add

    def sub(self, a, b):
        super().sub(a, b)
        LoggingCalculator.history.append(f'{a}-{b}={self.sub}')
        return self.sub

    def mul(self, a, b):
        super().mul(a, b)
        LoggingCalculator.history.append(f'{a}*{b}={self.mul}')
        return self.mul

    def div(self, a, b):
        super().div(a, b)
        LoggingCalculator.history.append(f'{a}/{b}={self.div}')
        return self.div


calc = LoggingCalculator()
print(calc.add(2, 3))
print(calc.mul(3, 3))
print(calc.sub(7, 4))
print(calc.div(5, 2))
print(calc.history)
