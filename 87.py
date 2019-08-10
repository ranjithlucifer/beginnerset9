n,m=input().split()
a=int(n)
b=int(m)
while(b):
    a,b=b,a%b
print(a)
