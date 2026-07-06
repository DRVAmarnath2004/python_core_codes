# #1.
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def is_passed(self):
#         return self.marks>40
#
#     def display(self):
#         print(f"name:{self.name}")
#         print(f"marks:{self.marks}")
# s1=Student("Amar",41)
# s2=Student("sohiel",30)
# print(s1.name,s1.is_passed())
# print(s2.name,s2.is_passed())


# #2.
# class Employee:
#     company_name="Tech corp"
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name=new_name
#
#     def display(self):
#         print(f"name:{self.name}")
#         print(f"company_name:{Employee.company_name}")
# emp1=Employee("Amar")
# emp2=Employee("Yaswnath")
#
# print("Before")
# emp1.display()
# emp2.display()
#
# Employee.change_company("cvcorp")
#
# print("After")
# emp1.display()
# emp2.display()
#
# #output:
# Before
# name:Amar
# company_name:Tech corp
# name:Yaswnath
# company_name:Tech corp
# After
# name:Amar
# company_name:cvcorp
# name:Yaswnath
# company_name:cvcorp

#3.
# class Math_ops:
#     def __init__(self,num):
#         self.num=num
#
#     @staticmethod
#     def is_even(num):
#         if num%2==0:
#             return True
#         else:
#             return False
#     def display(self):
#         print(f"num:{self.num}")
#
# num1=Math_ops(4)
# num1.display()
# print(Math_ops.is_even(num1.num))
#
# #output:
# num:4
# True
