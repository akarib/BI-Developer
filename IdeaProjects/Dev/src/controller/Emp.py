

class Employee:

    def __init__(self, first, last):

        self.first = first
        self.last = last
        self.full = first + '.' + last+"@company.com"

emp_1 = Employee('krb', 'Ala')

#emp_2 = Employee()



#emp_1.first = "krb"
#emp_1.last = "Ala"
#emp_1.full = emp_1.firstfirst +' '+emp_1.last


print(emp_1.full)

