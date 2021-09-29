def selsort(l):
    n=len(l)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if l[j]<l[min_index]:
                min_index=j
        l[min_index],l[i]=l[i],l[min_index]
l=[23,45,43,12,32,42,97]
selsort(l)
print(l)
        
