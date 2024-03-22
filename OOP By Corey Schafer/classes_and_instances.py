class Employee:
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1= Employee('ali', 'ahmed', 30000)
emp_2= Employee('hassan', 'ahmed', 43000)

print(emp_1.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))   ## This line does the same as the above. It takes instance as a argument of the method