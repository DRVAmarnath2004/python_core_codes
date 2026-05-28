#1.
# l=[21,22,23,24,25,26]
# k=list(map(lambda x:(x*9/5)+32,l))
# print(k)#[69.8, 71.6, 73.4, 75.2, 77.0, 78.8]

#2.
# l=["Amar","Snadeep","teja","Ganesh","Chiru","Raju"]
# k=list(filter(lambda x: x[0].isupper() ,l))
# m=[]
# m.append(k)
# print(m)#[['Amar', 'Snadeep', 'Ganesh', 'Chiru', 'Raju']]

#3.
# from functools import reduce
# l=[1,2,3,4,5]
# m=reduce(lambda x,y:x*y,l)
# print(m)#120

#4.
# l=[("Amar",21),("Gowtham",23),("Raju",20),("Sandeep",19)]
# k=sorted(l,key=lambda x:x[1],reverse=True)
# print(k)#[('Gowtham', 23), ('Amar', 21), ('Raju', 20), ('Sandeep', 19)]

#5.
# l=[1,2,3,4,5,6,7,8,9,10]
# k=list(map(lambda x:x**2 ,filter(lambda x:x%2==0,l)))
# m=list(filter(lambda x:x%2!=0,l))
# print(m)#[1, 3, 5, 7, 9]
# print(k)#[4, 16, 36, 64, 100]

#7.
# from functools import reduce
# l=['cat','elephant','dog','rhinoceros']
# k=reduce(lambda x,y:x if len(x)>len(y) else y,l)
# print(k)


