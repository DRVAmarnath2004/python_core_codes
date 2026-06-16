#1.
# def my_decorator(func):
#     def inner():
#         print("---Function is starting----")
#         func()
#         print("---Function id ended----")
#     return inner
# @my_decorator
# def greet():
#     print("Hello!")
# greet()

#2.
#2.1 with functools
# import functools
# def my_decorator(func):
#     def inner():
#         print("start")
#         func()
#         print("end")
#     return inner
# @my_decorator
# def greet():
#     print("hi hello")
# print(greet.__name__)

#2.2 without functools
# import functools
# def my_decorator(func):
#     @functools.wraps(func)
#     def inner():
#         print("start")
#         func
#         print("end")
#     return inner
# @my_decorator
# def greet():
#     """lets say hello"""
#     print("hi every one")
# print(greet.__name__)
# print(greet.__doc__)

