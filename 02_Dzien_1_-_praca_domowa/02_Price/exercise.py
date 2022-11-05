class Price:
    def __init__(self, price):
        self.price = price
        self.value = round(float(self.price), 2)

    def set_dolar(self, dolar):
        Price.from_usd = dolar * 3.8
        self.__init__(Price.from_usd)

    def set_euro(self, euro):
        Price.from_eur = euro * 4.5
        self.__init__(Price.from_eur)

    def __str__(self):
        return f'{self.value}zł'


s = Price(10)
print(s.__str__())
s.set_euro(2.5)
print(s.__str__())
s.set_dolar(13.3)
print(s.__str__())