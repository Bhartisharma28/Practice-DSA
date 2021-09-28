def TOH(n,A,B,C):
    if n==1:
        print(A, "to", C)
    else:
        TOH(n-1,A,C,B)
        print(n,A,C)
        TOH(n-1,B,A,C)
TOH(3,'A','B','C')
