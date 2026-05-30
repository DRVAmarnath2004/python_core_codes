#2.
a=[1,2,3,4]
b=[10,20,30,40]
c=[]
k=list(map(lambda x,y:x+y,a,b))
c.append(k)
print(c)#[[11, 22, 33, 44]]

#3.
l=[12,15,7,18,20,21,25]
k=list(filter(lambda x:(x%3==0)!=(x%5==0),l))
print(k)#[12, 18, 20, 21, 25]

#4.
from functools import reduce
l = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, l, 10)
print(result)#20

#5.
nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x.append(10), nums))
print("Result:", result)#Result: [None, None, None]
print("Nums:", nums)#Nums: [[1, 2, 10], [3, 4, 10], [5, 6, 10]]

#6.
l=[[1,2],[3,4],[5,6]]
k=list(map(lambda x:x.append(5),l))
print(l)#[[1, 2, 5], [3, 4, 5], [5, 6, 5]]

#7.
l=[("apple",100),("banana",40),("cherry",150)]
k=list(filter(lambda x:x[1]>50 ,l))
print(k)#[('apple', 100), ('cherry', 150)]

#8.
from functools import reduce
a=int(input())
b=int(input())
k=reduce(lambda x,y:x if x>y else y,[a,b])
print(k)#20

#9.
l=["A","m"]
k=list(map(lambda x:ord(x),l))
print(k)#[65, 109]

##10.
l="Amar"
k=list(filter(lambda x:x not in "AEIOUaeiou",l))
print(k)#['m', 'r']

#11.
from functools import reduce
l=['P','y','t','h','o','n']
k=reduce(lambda x,y:x+y,l)
print(k)#Python

#12.
l=[10,350,10,350,20]
k=list(map(lambda x:id(x),l))
print(k)#[2724096639504, 2724097686096, 2724096639504, 2724097686096, 2724096639824]

#13.
from functools import reduce
l = [5, 10, 15, 20, 25, 30]
k = reduce(lambda x, y: x + y,filter(lambda x: x % 5 == 0,map(lambda x: x**2, l)))
print(k)#2275