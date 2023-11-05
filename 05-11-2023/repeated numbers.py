#smart interviews primary- Repeated numbers
#optimized code using two pointers
# Enter your code here. Read input from STDIN. Print output to STDOU
t=int(input())
for _ in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    p1=0
    p2=p1+1
    lst.sort()
    while p1<p2 and p2<len(lst):
        if lst[p1]==lst[p2]:
            print(lst[p1],end=' ')
        p1+=1
        p2+=1
    print()

            


