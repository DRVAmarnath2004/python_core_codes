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

#4.
# class Car:
#     wheels=4
#     def __init__(self,mileage):
#         self.mileage=mileage
#     @classmethod
#     def change_wheels(cls,wheel):
#         cls.wheels=wheel
#     def display_specs(self,):
#         print(f"mileage:{self.mileage}")
#         print(f"wheels:{Car.wheels}")
#
# car1=Car(250)
# car2=Car(350)
#
# print("Before")
# car1.display_specs()
# car2.display_specs()
#
# Car.change_wheels(6)
# print("After")
# car1.display_specs()
# car2.display_specs()
# #output:
# Before
# mileage:250
# wheels:4
# mileage:350
# wheels:4
# After
# mileage:250
# wheels:6
# mileage:350
# wheels:6

#5.
# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     @staticmethod
#     def to_fah(celsius):
#         return (celsius*9/5)+32
#     def show_conversion(self):
#         fah=Temperature.to_fah(self.celsius)
#         print(f"Celsius:{self.celsius}")
#         print(f"Fahrenheit: {fah}°F")
#
#
# t1 = Temperature(25)
# t2 = Temperature(100)
#
# t1.show_conversion()
# print()
# t2.show_conversion()
# #output:
# Celsius:25
# Fahrenheit: 77.0°F
#
# Celsius:100
# Fahrenheit: 212.0°F

# #6.
# class Book:
#     total_books = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.total_books += 1
#
#     @classmethod
#     def from_string(cls, book_str):
#         title, author = book_str.split("-")
#         title = title.strip()
#         author = author.strip()
#
#         if cls.is_valid_title(title):
#             return cls(title, author)
#         else:
#             return "Invalid book title"
#
#     @staticmethod
#     def is_valid_title(title):
#         return len(title) >= 3
#
#
#
# b1 = Book.from_string("Harry Potter - J.K. Rowling")
# b2 = Book("The Song of Ice and Fire", "R.R. Martin")
#
#
# print("Book 1:")
# print(b1.title)
# print(b1.author)
#
# print("\nBook 2:")
# print(b2.title)
# print(b2.author)
#
# print("\nTotal Books:", Book.total_books)

#7.
# class Employee:
#     bonus_rate=0.1
#     def __init__(self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#
#     def final_salary(self):
#         return self.base_salary+(self.base_salary*Employee.bonus_rate)
#     @classmethod
#     def update_bonus(cls,new_rate):
#         cls.bonus_rate=new_rate
#     @staticmethod
#     def valid_salary(sal):
#         return sal>0
# emp1=Employee("Amar",6000000)
# emp2=Employee("Yash",8000000)
#
# print("--------before---------")
# print(emp1.final_salary())
# print(emp2.final_salary())
# emp1.update_bonus(0.2)
# print("--------After-----------")
# print(emp1.final_salary())
# print(emp2.final_salary())

#output:
# --------before---------
# 6600000.0
# 8800000.0
# --------After-----------
# 7200000.0
# 9600000.0

# #8.
# class Course:
#     total_students=0
#     def __init__(self,student_name):
#         self.student_name=student_name
#     def enroll(self):
#         Course.total_students+=1
#     @classmethod
#     def show_total(cls):
#         print("Total Students:",cls.total_students)
#     @staticmethod
#     def is_eligible(age):
#         if age>=18:
#             return True
#         else:
#             return False
# s1=Course("Amar")
# s2=Course("Sandeep")
# if Course.is_eligible(21):
#     s1.enroll()
# if Course.is_eligible(20):
#     s2.enroll()
# Course.show_total()
#
# output:
# Total Students: 2

#9.
class BankAccount:
    bank_name="HDFC"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"{amount} deposited.")
            print("Balance:", self.balance)
        else:
            print("Invalid amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0
a1 = BankAccount("Amar", 5000)
a2 = BankAccount("Sandeep", 8000)
a1.deposit(2000)
a2.deposit(500)
BankAccount.change_bank_name("SBI")

print("Bank Name:", BankAccount.bank_name)