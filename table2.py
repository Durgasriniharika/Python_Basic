#print the multiplication table of a given number n  up to R terms (starting from 1)
#for loop
n,r=map(int,input().split())
for i in range(1,r+1,1):
    print(f"{n}x{i}={n*i}")
#while loop
i=1
while i<=r:
    print(n,"*",i,"=",n*i)#(f"{n}x{i}={n*i}")
    i=i+1
    
