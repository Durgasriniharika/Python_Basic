#ronaldo is watching a football match.the current score is a-b.that is team 1 has scored A goals and team to has b goals.
#ronaldo wonders if it is possible for the score to become c-d at a later point in the game(i.e team 1 has scored c goals and team 2 has scored b goals).
a,b=map(int,input().split())
c,d=map(int,input().split())
if c>a or d>b:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
