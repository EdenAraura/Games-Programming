##method - funct associated with class
##class - group of code. blueprint for creating instances
##instance variables - data unique to each instance

class Developer:
    ##self is the first instance; self is generic name for instances (i.e. self == emp1 & emp2)
    ##self is what the object passes through as, the following delcarations are attributes of the class
    ##init is the argument that creates the objects
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@gmail.co.uk"

    def fullname(self):
        print("{0}, {1}".format(self.last, self.first))

    
              
emp1 = Developer("David", "Prue", 32000)
emp2 = Developer("Sandal", "Nee", 28000)
##separate instances of the same class

#emp1.first = "Cory"
#emp1.last = "Prue"
#emp1.email = "prue@gmail.com"
#emp1.pay = 32000

#emp2.first = "Sheldon"
#emp2.last = "Nee"
#emp2.email = "snee@hotmail.co.uk"
#emp2.pay = 28000
##classes set this automatically

print(emp1.email)
print(emp2.email)

#print(emp1.fullname() + emp2.fullname())

##for some reason prints "none" after
#print(emp1.fullname())
Developer.fullname(emp1)
