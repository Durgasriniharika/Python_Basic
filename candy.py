#ram received N candies on birthday.he wants to put these candies in some bags.a bag has K pockets and each pocket can hold at most M candies.
#find the minimum number of bags ram needs so that he can put every candy into a bag.
n,k,m=map(int,input().split())
if n%(k*m)==0:
    print(n//(k*m))
else:
    print(n//(k*m)+1)
