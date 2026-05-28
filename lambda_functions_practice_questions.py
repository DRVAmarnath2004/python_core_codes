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


