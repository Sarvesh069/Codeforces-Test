def code(w):
    u,l=0,0
    for i in w:
        if i.isupper():
            u+=1
        else:
            l+=1
    if u<=l:
        return w.lower()
    else:
        return w.upper()
w=input()
print(code(w))