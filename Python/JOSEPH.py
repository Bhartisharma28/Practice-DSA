def JOS(n,p):
    if n==1:
        return 0
    else:
        return (JOS(n-1,p)+p)%n
print(JOS(5,3))
