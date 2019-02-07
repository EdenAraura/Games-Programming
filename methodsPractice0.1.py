
class Developer:

    incr = 1.07
    teamNum = 0

    ##runs on every creation of an instance
    def __init__(self, first, last, pay):
        global teamNum
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@gmail.co.uk"

        Developer.teamNum += 1

    def fullname(self):
        print("{0}, {1}".format(self.last, self.first))

    ##methods can be used to edit init's values 
    def bonus(self):
        self.pay = int(self.pay * self.incr)

    @classmethod
    def setRaise(clss, amnt):
        clss.incr = amnt

    @classmethod
    def fromStr(clss, empStr):
        first, last, pay = first, last, pay = empStr.split("-")
        print(clss(first, last, pay))
              
emp1 = Developer("David", "Prue", 32000)
emp2 = Developer("Sandal", "Nee", 28000)

emp3 = "Jane-Doe-42000"
emp4 = "Fran-Lisbon-34000"
emp5 = "Reg-Stern-22000"
newEmp = Developer.fromStr(emp3)

##setRaise changes the incr amount
Developer.setRaise(1.05)

print(emp1.__dict__)

print(emp1.incr)
print(emp2.incr)
print(Developer.incr)
emp1.bonus()
print(emp1.pay)

print(Developer.teamNum)

print(emp3.pay)
#print(Developer.__dict__)
