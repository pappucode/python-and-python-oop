class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Pappu", "Akondo", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# Both do the same 
print(emp_1.fullname())
print(Employee.fullname(emp_2))
