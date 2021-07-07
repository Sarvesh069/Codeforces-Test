def code(num):
    c=0
    for i in num:
        if i=='4' or '7':
            c+=1 
    if c==4 or c==7:
        return "YES"
    return "NO"
num=input()
print(code(num))