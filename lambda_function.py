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

