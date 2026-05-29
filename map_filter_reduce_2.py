#2.
# a=[1,2,3,4]
# b=[10,20,30,40]
# c=[]
# k=list(map(lambda x,y:x+y,a,b))
# c.append(k)
# print(c)#[[11, 22, 33, 44]]

#3.
# l=[12,15,7,18,20,21,25]
# k=list(filter(lambda x:(x%3==0)!=(x%5==0),l))
# print(k)#[12, 18, 20, 21, 25]

#4.
# from functools import reduce
# l = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, l, 10)
# print(result)#20

#5.
# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))
# print("Result:", result)#Result: [None, None, None]
# print("Nums:", nums)#Nums: [[1, 2, 10], [3, 4, 10], [5, 6, 10]]

#6.
# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x.append(5),l))
# print(l)#[[1, 2, 5], [3, 4, 5], [5, 6, 5]]

#7.
# l=[("apple",100),("banana",40),("cherry",150)]
# k=list(filter(lambda x:x[1]>50 ,l))
# print(k)#[('apple', 100), ('cherry', 150)]

#8.
# from functools import reduce
# a=int(input())
# b=int(input())
# k=reduce(lambda x,y:x if x>y else y,[a,b])
# print(k)#20

#9.
# l=["A","m"]
# k=list(map(lambda x:ord(x),l))
# print(k)#[65, 109]

#10.
# l=["Amar","Raju"]
# k=list(filter(lambda x:x,map(lambda x : x not in "AEIOUaeiou",l)))
# print(l)