#tom has N friends.tom promised that he would gift a pair of shoes(consisting of one left shoe and one right shoe) to each of his N friends.
#tom was about to go to the marketplace to buy shoes.but he suddenly remembers that he already had M left shoes.
#what is the minimum number of extra shoes that tom will have to buy to ensure that he is able to gift a pair of shoes to each of his n friends.
#ex:- if n=2,m=4,the tom already has 4 left shoes,so he must buy 2 extra right shoes to form 2 pairs of shoes.
#therefore tom must buy atleast 2 extra shoes to ensure that he is able to get 2 pairs of shoes.
n,m=map(int,input().split())
if m>=n:
    print(n)
else:
    print(n+(n-m))
