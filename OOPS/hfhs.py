class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("John", 50000)
e2 = Employee("Faiz", 60000)
e3 = Employee("Kaif", 55000)
print(e1.company)
print(e3.name)
print(e3.salary)
    