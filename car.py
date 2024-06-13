#a single car can acccommodate at most 4 people.N friends want to go to a restaurent for a party.
#find the minimum number of cars required to accommodate all the friends.
n=int(input())
if n%4==0:
    print(n)
else:
    print((n//4)+1)
