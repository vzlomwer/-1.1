class Car:
    millc = 'volkswagen'
    def __init__(self ,model ,year, price, millc = 'volkswagen'):
        self.model = model
        self.year = year
        self.price = price


cr1 = Car("golf", 2022, "100000$")
print(cr1.millc)
print(cr1.model)
print(cr1.year)
print(cr1.price)



cr2 = Car("golf", 2021, "90000$")
print(cr2.millc)
print(cr2.model)
print(cr2.year)
print(cr2.price)


cr3 = Car("multivan", 2022, "400000$")
print(cr3.millc)
print(cr3.model)
print(cr3.year)
print(cr3.price)

cr4 = Car("t5", 2012, "15000$")
print(cr4.millc)
print(cr4.model)
print(cr4.year)
print(cr4.price)


cr5 = Car("t6", 2020, "200000$")
print(cr5.millc)
print(cr5.model)
print(cr5.year)
print(cr5.price)


cr6 = Car("t7", 2022, "300000$")
print(cr6.millc)
print(cr6.model)
print(cr6.year)
print(cr6.price)












class Cat:
    cats = 'cat'
    def __init__(self ,name,year, color, breed):
        self.name = name
        self.year = year
        self.color =color
        self.breed =breed


ct1 = Cat("Misti", 4 , "colorful", "not breed")
print(ct1.name)
print(ct1.year)
print(ct1.color)
print(ct1.breed)


ct2 = Cat("Marsik", 3 , "grey", "oar-eared")
print(ct2.name)
print(ct2.year)
print(ct2.color)
print(ct2.breed)
