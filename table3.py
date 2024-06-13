#you"ll be given three numbers N,A and B.print the multiplication table of number n
n,a,b=map(int,input().split())
for i in range(a,b+1,1):
    print(f"{n} x {i} ={n*i}")
#while
i=a
while i<=b:
    print(f"{n} x {i} ={n*i}")
    i+=1
