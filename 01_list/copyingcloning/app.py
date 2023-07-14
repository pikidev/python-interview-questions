def cloning(list):
    newList= list[:]
    return newList


l1 = [4, 8, 2, 10, 15, 18]
l2= cloning(l1)
print("Original List:", l1)
print("After Cloning:", l2)
  
