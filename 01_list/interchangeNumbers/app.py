# Python3 program to swap first
# and last element of a list

# Swap function
#len() function returns the number of items in an object.

def swaplist(nl):
    size= len(nl)

    temp=nl[0]
    nl[0]=nl[size-1]
    nl[size-1]=temp
    return nl

newList = [12, 35, 9, 56, 24]
print(swaplist(newList))

