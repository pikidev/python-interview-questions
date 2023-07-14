

def countX(list,x):
    count = 0
    for i in list:
        if(i==x):
            count=count+1
    return count
    
list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occured {} times'.format(x,countX(list,x)))


