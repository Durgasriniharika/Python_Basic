#math man considers a number Y as magical if and only if its divisible by X and not divisible by Z.
#given x,y,z find out if y is magical or not magical.
x,y,z=map(int,input().split())
if y%x==0 and y%z!=0:
    print("MAGICAL")
else:
    print("NOT MAGICAL")
