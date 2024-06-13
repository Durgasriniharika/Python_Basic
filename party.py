#rajesh wants to give a burger party to all the N friends i.e he wants to buy one burger for each of his frnds.the cost of each burger is X rupees while rajesh has a total of K rupees with him.determine whether he has enough money to buy a burger for each of his friends or not.
n,x,k=map(int,input().split())
if k>=(n*x):
    print("yes")
else:
    print("no")
