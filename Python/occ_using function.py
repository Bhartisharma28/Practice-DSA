def occ(l,x):
    count=0
    for i in l:
        if i==x:
            count+=1
    return count
l=[10,20,30,40,30,30,20,30]
print(occ(l,20))
