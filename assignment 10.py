#QUE1
class Animal:
    def __init__(self,name):
        self.name=name
    def animal(self):
        print("animal name is"+self.name)
class Tiger(Animal):
   pass

a1=Animal("tiger")
a1.animal()

#QUE 2
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'b'
a = A()
b= B()
print (a.f(),b.f())

#QUE3
class Cop:
    def __init__(self,name,age,wk,ex,des):
        self.name=name
        self.age=age
        self.work=wk
        self.experiance=ex
        self.designation=des
    def Add(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experiance)
        print(self.designation)
    def update(self,name,age,wk,ex,des):
        self.name
        self.age
        self.work
        self.experiance
        self.designation
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experiance)
        print(self.designation)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experiance)
        print(self.designation)
c1 = Cop("tarun", 21, "gun man", 4, "co")
class Mission(Cop):
    def add_mission_detail(self):
        print('mission comp')
b=Mission("abhi",23,"fire man",5,"po")
b.display()
b.update('"vanu',21,"wrkin",4,"mo")

#QUE 5
class Shape():
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
class Rectangle(Shape):
    def Area(self):
        area=(self.l)*(self.b)
        print(area)
class Square(Shape):
    def Area(self):
        AREA=(self.l)*(self.l)
        print(AREA)
s=Shape(12,5)
r=Rectangle(12,5)
r.Area()
sq=Square(4,4)
sq.Area()


