#in the medieval age,there were 3 kingdoms a,b,c.the army of these kingdom had Na,Nb,Nc soilders respectively.
#you are given that an army with X soilders can defeat anarmy with Y soilders only if x>y.
#an army is said to be dominant if it can defeat both the other armies combined.
#for example,kingdom c's army will be dominant only if Nc>Nb>Na.
#determine whether any kingdom is dominant than others or not? 

a,b,c=map(int,input().split())
if a>(b+c) or b>(a+c) or c>(a+b):
    print("YES")
else:
    print("NO")
