def bs(l,x):
    low=0
    high=len(l)-1
    while low<high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            high=mid+1
        else:
            high=mid-1
    return -1
l=[20,30,40,50,60,70,100]
bs(l,60)
