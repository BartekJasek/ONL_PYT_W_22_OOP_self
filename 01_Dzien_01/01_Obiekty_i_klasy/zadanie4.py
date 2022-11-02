class Employee:
    def __init__(self, id, first_name, last_name, salary=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = salary

    def set_salary(self, new_salary):
        if isinstance(new_salary, int) and new_salary >= 0:
            self._salary = new_salary


s = Employee(1, 'Bartek', 'Jasek')
s.set_salary(1000)
