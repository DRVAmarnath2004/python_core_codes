# def fun(*a):
#    print(a)
#    print(*a)
# fun(10,10,30,40,60)

# def fun3(a,b,c,d):
#   print(a,b,c,d)
# def fun2(**b):
#   print(b)
#   fun3(**b)
# fun2(a=75,b=30,c=40,d=70)

# def fun5(*a,*b):
#   print(a,b,sep="\n")
# fun5(10,1,5,3,8,6,7,10)

# def fun5(*a,**b):
#    print(a,b,sep="\n")
# fun5(10,7,a=30,b=57)

# def fun6(*a):
#     even=[]
#     for num in a:
#         if(num%2==0):
#             even.append(num)
#             print(num)
#     total=sum(even)
#     print("total :",total)
#
# fun6(1,7,8,25,30,60,70)

def fun7(*a):
    even_position_items = []
    odd_position_items = []
    sum=0

    for i, num in enumerate(a):
        if i % 2 == 0:
            even_position_items.append(num)
            sum+=num
            print(sum)




fun7(1, 2, 3, 4, 5, 7, 7, 8, 8, 10)


