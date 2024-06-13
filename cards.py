#king is playing a varient of blackpack,where 3 numbers are drawn and each number lies between 1 and 10(with both 1 and 10 inclusive).
#king wins the game when the sum of these 3 numbers is exactly 21?
#given the first two numbers A and B that have been drawn by king.what should be 3rd number that should be drawn by the king in order to win the game?
#note that it is possible that king cannot win the game.no matter what is the 3rd number.in such cases,report -1 as the answer.
a,b=map(int,input().split())
if(a+b)>=11: # or ((21-(a+b))>=1) and ((21-(a+b))<=10)
    print(21-(a+b))
else:
    print("-1")
