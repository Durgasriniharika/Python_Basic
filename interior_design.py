#stark decided to redecorate his house and now needs to decide between two diferent styles of interior design.
#for the first styl,tiling the floor will cost X1 rupees and painting the walls will cost Y1 rupees.
#for the second style,tiling the floor will cost X2 rupees and painting walls will cost Y2 rupees.
#stark will choose which ever style has the lower total cost.how much will stark pay for his interior design?
x1,y1,x2,y2=map(int,input().split())
if (x1+y1)<=(x2+y2):
    print("money",x1+y1)
else:
    print(x2+y2)
