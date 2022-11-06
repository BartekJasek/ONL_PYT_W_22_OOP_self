class Price23Vat:
    def __init__(self, brutto):
        self._brutto = brutto
        self._netto = self._brutto / 1.23
        self._tax = self._brutto - self._netto

    @property
    def brutto(self):
        return self._brutto

    @property
    def netto(self):
        return self._netto

    @property
    def tax(self):
        return self._tax

    @brutto.setter
    def brutto(self, value):
        new_brutto = value
        self.__init__(new_brutto)

    @netto.setter
    def netto(self, value):
        new_brutto = value * 1.23
        self.__init__(new_brutto)

    @tax.setter
    def tax(self, value):
        new_brutto = (value / 23) * 123
        self.__init__(new_brutto)


price = Price23Vat(123)

print(price.brutto)        # 123
print(price.tax)           # 23
print(price.netto)         # 23

price.tax = 69

print(price.brutto)        # 369
print(price.tax)           # 69
print(price.netto)         # 300
