n=int(input())
for i in range((n//2)):
    print(" ",end='')
print("*",end='')
c=1
print()
for i in range(n//2-1,-1,-1):
    for j in range(i):
        print(" ",end='')
    print("*",end='')
    for j in range(c):
        print(" ",end='')
    print("*")
    c+=2
c=c-2
#second part
for i in range(1,n//2):
    for j in range(i):
        print(" ",end='')
    print("*",end='')
    for j in range(c-2):
        print(" ",end='')
    print("*")
    c-=2
for i in range((n//2)):
    print(" ",end='')
print("*",end='')

    
        
    
