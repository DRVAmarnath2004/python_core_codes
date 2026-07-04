# class Student:
#     total=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.total+=1
#     def display(self,phoneno,branch):
#         print(f"Name:{self.name}")
#         print(f"age:{self.age}")
#         print(f"phoneno:{phoneno}")
#         print(f"branch:{branch}")
# s1=Student(name="Amar",age=21)
# s2=Student(name="ram",age=22)
# s3=Student(name="light",age=23)
# s1.display(7416889989,"cse")
# Student.display(s1)

# Student.total+=1
#
# print(s1.total)
# print(s2.total)
# print(s3.total)
# print(Student.total)
#
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)

#1.
# class Car:
#     fuel_type="petrol"
#     def __init__(self,make,model,year,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price
#     def display(self):
#         print(f"make:{self.make}")
#         print(f"model:{self.model}")
#         print(f"year:{self.year}")
#         print(f"price:{self.price}")
#         print(f"Fuel type:{Car.fuel_type}")
# car1=Car(make="Tata",model="fort",year=2013,price=1000000)
# car2=Car(make="Swift",model="",year=2015,price=2000000)
# car1.display()
# print()
# car2.display()

#3.
class Employee:
    employee_count=0.
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.employee_count+=1
    def display(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"salary:{self.salary}")
emp1=Employee("amar",21,500000)
emp2=Employee("raju",22,600000)
emp3=Employee("chiru",21,70000)
emp4=Employee("sohail",21,800000)
emp1.display()
emp2.display()
emp3.display()
emp4.display()
print(Employee.employee_count)
