def bs(l,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if l[mid]==x:
        return mid
    elif l[mid]>x:
        return bs(l,x,low,mid-1)
    else:
        return bs(l,x,mid+1,high)

l = [ 2, 3, 4, 10, 40 ]
print(bs(l,40,0,len(l)-1))

  
