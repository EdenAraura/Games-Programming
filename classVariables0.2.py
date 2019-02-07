
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
              
emp1 = Developer("David", "Prue", 32000)
emp2 = Developer("Sandal", "Nee", 28000)

##declaring this variable created the incr attribute under the emp 1 instance, rather than accessing it from the init - meaning it can be altered seperate to the init
emp1.incr = 1.03

print(emp1.__dict__)

print(emp1.incr)
print(emp2.incr)
print(Developer.incr)
emp1.bonus()
print(emp1.pay)

print(Developer.teamNum)
#print(Developer.__dict__)
