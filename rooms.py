#six friends go on a trip and are looking for acccomdation.after looking for hours,
#they find a total which offers two types of rooms-double rooms and triple.a double room costs rs.X.while a triple room costs rs.Y
#the friends can either get three double rooms or get two triple rooms.find the minimum amount they will have to pay to accomdate all six of them?
x,y=map(int,input().split())
if (3*x)<=(2*y):
    print("cost",3*x)
else:
    print(2*y)
