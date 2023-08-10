def f(seq):
    n=len(seq)
    L=[0]*(n-1)+[1]
    for i in range(n-2,-1,-1):
        if seq[i]<seq[i+1]:
            L[i]=1+L[i+1]
            print(L)
        else:
            L[i]=1
    return max(L)
print(f([2,3,1,4,6]))