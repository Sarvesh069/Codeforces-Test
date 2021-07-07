def code(n,ls):
    k=[]
    for i in range(1,n+1):
        if i in ls:
            k.append(ls.index(i)+1)
    for i in k:
        print(i,end=" ")
n=int(input())
ls=list(map(int,input().strip().split(" ")))[:]
code(n,ls)