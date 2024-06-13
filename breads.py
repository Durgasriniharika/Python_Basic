#wanda loves bread.she has N loaves of bread,all of which expire after exactly M days.she can eat upto K loaves of bread in a day.
#can she eat all the loaves of bread.before they expire?
n,m,k=map(int,input().split())
if n<=m*k:
    print("yes")
else:
    print("no")
    
