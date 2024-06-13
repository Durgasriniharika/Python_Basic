#print the multiplication table of the given number N upto 12 terms (starting from 1)
n=int(input())
for i in range(1,13,1):
    print(f"{n} x {i}= {n*i}")
#while
i=1
while i<=12:
    print(n,"*",i,"=",n*i)#(f"{n}x{i}={n*i}")
    i=i+1
    
