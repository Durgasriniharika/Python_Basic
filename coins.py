#kohli has infinite coins in denominations of rupees 5 and rupees 10.
#find the minimum number of coins kohli needs to pay exactly X rupees.if it is impossible to pay X rupees in denominations of rupees 5 and 10 only,print "-1".
x=int(input())
if x%5==0 or x%10==0:
    print("min number of coins",x//10+(x%10)//5)
else:
    print("-1")
