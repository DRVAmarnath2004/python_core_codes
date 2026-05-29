#-------Lambda-------------------------
# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x.append(5),l))
# print(l)

#--------Filter-----------------

 # l=[1,2,3,4,5,6,7,8,9]
 # e=[]
 # for i in l:
 #     if i%2==0:
 #         e.append(i) # when we use normally we will get this

# if we use lambda and filter

# l=[1,2,3,4,5,6,7,8,9,10]
# e=list(filter(lambda x:x%2==0,l))
# print(e) # [2, 4, 6, 8, 10]

# l=[1,2,3,4,5,6,7,8,9,10]
# e=list(map(lambda x:x%2==0,l))
# print(e) # [False, True, False, True, False, True, False, True, False, True]

# l=[1,2,3,4,5,6,7,8,9,10]
# e=list(filter(lambda x:x%2,l))
# print(e)#[1, 3, 5, 7, 9]

# l=[3,6,1,2,5,9,12,16]
# e=list(filter(lambda x:x%3,l))
# print(e)#[1, 2, 5, 16]

# a = "Amar"
# v = "aeiouAEIOU"
# k = list(filter(lambda x: x not in v, a))
# print(k)#['m', 'r']

# l=[1,7,8,12,14,21,22,63,66]
# e=list(map(lambda x:x**3 ,l))
# k=list(filter(lambda x:x%4,e))
# print(k)#[1, 343, 9261, 250047]
# print(e)#[1, 343, 512, 1728, 2744, 9261, 10648, 250047, 287496]

#-----if we want in a single statement of the above one then-----
# l=[1,7,8,12,14,21,22,63,66]
# e=list(filter(lambda x:x%4,map(lambda x:x**3,l)))
# print(e)#[1, 343, 9261, 250047]

#----------3.Reduce----------------------

from functools import reduce
# l=[1,7,8,12,14,21,22,63,66]
# m=reduce(lambda x,y:x+y,l)
# print(m)

#------Sorted------------------------------
# l=[21,3,2,5,22,6,32]
# k=sorted(l,key=lambda x:x%3)
# print(k)#[21, 3, 6, 22, 2, 5, 32]

# l=[23,21,27,28,44,46]
# k=sorted(l,key=lambda x:x%7,reverse=True)
# m=sorted(l,key=lambda x:x%7,reverse=False)
# print(k)#[27, 46, 23, 44, 21, 28] this value is occur is reverse is true means descending order of remainders
# print(m)#[21, 28, 23, 44, 46, 27] this value is occur is reverse is false means ascending order of remainders

#-------functional references------------------
#1.
# count=len
# l=[1,2,3,4,56,7,8]
# print(count(l))

