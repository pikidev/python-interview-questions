
lst = [12, 67, 98, 34]
x=list(map(lambda ele: sum(int(sub) for sub in str(ele)),lst))
print(str(x))


