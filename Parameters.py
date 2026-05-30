#1.
def mul(a,b,c):
    return a*b*c
print(mul(1,2,3))#6

#2.
def pet_name(a,b):
    return f"My {a} is named {b}"
print(pet_name("cat","chiru"))#My cat is named chiru

#3.
def names(a,b,c):
    return a , b
print((names("Amar","arjun")))#TypeError: names() missing 1 required positional argument: 'c'

#4.
def power(base,expo):
    return base**expo
print(power(10,2))#100

#5.
def full_name(first,middle,last):
    return first, middle ,last
print(full_name("Amarnath","Rama Venkata","Devarasetty"))#('Amarnath', 'Rama Venkata', 'Devarasetty')

