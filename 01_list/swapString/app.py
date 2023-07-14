
# Python3 code to demonstrate
# Swap elements in String list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
print(str(test_list))
res = ", ".join(test_list)
res= res.replace("G","_").replace("e","G").replace("_","e").split(',')
print(str(res))
 
