#alice is playing air hockey with bob.the first person to earn seven points win the match.
#currently,alice's score is A and bob's score is B.charlie is eagerly waiting for his turn.
#help charlie by calculating the minimum number of points that will be further scored in the match before it ends.
a,b=map(int,input().split())
if a==b:
    print("minimum points",7-b)
elif a>b:
    print("minimum points",7-a)
else:
    print("minimum points",7-b)
