a,b=input().split()
x=int(a)
y=int(b)
if x > y:  
    s=x  
else:  
    s=y  
while(True):  
    if((s%x==0) and (s%y==0)):  
        lcm=s  
        break  
    s+= 1  
print(lcm)  
