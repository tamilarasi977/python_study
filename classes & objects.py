# Class create syntax:

class MyClass:
    x=5
print("MyClass")


# Object create syntax:

class MyClass:
    x=6
obj=MyClass()
print(obj.x)    


#Use the __init__() function to assign values to object properties:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Person("tamil",28)  
print(obj.name)
print(obj.age)  


# Modify the objects:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("tamil",24)
p1.age=30
print(p1.age)


# Delete the objects:

class Person:
    def __init__(self,name):
        self.name=name
p1=Person("tamil")
del p1
print(p1) 




