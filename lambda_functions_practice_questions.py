#1.
# l=[1,2,3,4,5,6]
# k=list(map(lambda x:x**3,l))
# print(k)

#2.
# l=[1,2,10]
# m=[3,4,5]
# k=list(map(lambda x,y:x if x>y else y,l,m))
# print(k)

#3.
# l=[1,2,3,4,5,6,7,8,9]
# k=list(map(lambda x:x%2==0,l))
# print(k)

#4.
# l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# l.sort(key=lambda x:x[1])
# print(l)

#5.
# def square(x):
#     return x * x
#
# k = lambda n: square(n)
# 
# print(k(5))