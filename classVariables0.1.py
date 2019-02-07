
class Developer:

    incr = 1.07

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@gmail.co.uk"

    def fullname(self):
        print("{0}, {1}".format(self.last, self.first))

    ##methods can be used to edit init's values 
    def bonus(self):
        self.pay = int(self.pay * self.incr)
              
emp1 = Developer("David", "Prue", 32000)
emp2 = Developer("Sandal", "Nee", 28000)

print(emp1.incr)
print(Developer.incr)
emp1.bonus()
print(emp1.pay)
