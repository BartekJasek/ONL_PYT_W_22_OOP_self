class Price23Vat:
    def __init__(self, brutto):
        self._brutto = brutto
        self._netto = self._brutto / 1.23
        self._tax = self._brutto - self._netto

    def get_brutto(self):
        return self._brutto

    def get_netto(self):
        return self._netto

    def get_tax(self):
        return self._tax

    def set_brutto(self, value):
        new_brutto = value
        self.__init__(new_brutto)

    def set_netto(self, value):
        new_brutto = value * 1.23
        self.__init__(new_brutto)

    def set_tax(self, value):
        new_brutto = (value / 23) * 123
        self.__init__(new_brutto)


s = Price23Vat(10)
s.set_brutto(100)
print(s.get_brutto())
print(s.get_netto())
print(s.get_tax())


s.set_netto(100)
print(s.get_brutto())
print(s.get_netto())
print(s.get_tax())

s.set_tax(100)
print(s.get_brutto())
print(s.get_netto())
print(s.get_tax())
