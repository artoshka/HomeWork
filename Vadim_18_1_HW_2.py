class Company:


    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name



class Person(Company):


    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def get_salary(self):
        if self.company_bank < self.salary:
            print("У вас недостаточно средств!")
        else:
            self.company_bank -= self.salary
            print(f"Вы дали зарплату {self.first_name} В размере {self.salary}$\nВаш капитал:{self.company_bank}$\n")



    def person_info(self):
        print(f"Имя: {self.first_name}\nФамилия: {self.last_name}\nЗарплата: {self.salary}")

SunPy = Company(90000, "SunPy")
Sanya = Person(SunPy.company_bank, SunPy.company_name, "Антон", "Киров", 1500)

Sanya.get_salary()


Sanya.person_info()
