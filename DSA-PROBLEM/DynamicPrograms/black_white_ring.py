#Choose a circular continuous segment of the array and perform a left cyclic shift on the chosen segment.

# cook your dish here
t=int(input())
for i in range(t):
    accept=int(input())
    array=list(map(int,input().split()))
    o=e=0
    for j in range(len(array)):
        if(array[j]==array[(j+1)%accept]):
            if(array[j]==1):
                e+=1
            else: o+=1
    create=min(e,o)
    if(create%2==0): print("Bob")
    else:
        print("Alice")