# #method1
# c=3
# d=1
# print(min(c,d))

# # mthod2

# def min(a,b):
#     if a<=b:
#         return a
#     else:
#         return b    
# c=3
# d=1
# print(min(c,d))

# method3

from functools import reduce
c=3
d=1
min = reduce(lambda x,y: x if x<y else y,[c,d] )
print(min)




    

 
