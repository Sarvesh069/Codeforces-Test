def code(n,word):
    if len(word)<=10:
        print(word)
    else:
        print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")
n=int(input())
for i in range(n):
    word=input()
    code(n,word)