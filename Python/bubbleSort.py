def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=[12,32,54,45,76,56]
bubblesort(l)
print(l)
