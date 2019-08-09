n=input()
c=len(n)
a=[]
b=[]
for i in range(0,c):
    if i%2==0:
        print(n[i],end="")
print("",end=" ")   
for i in range(0,c):
    if i%2!=0:
        print(n[i],end="")
