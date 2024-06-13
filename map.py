a,b,c=map(int,input(),split())
#for output
#two methods
#1.f string
#2. dot formatting method
#--->1.using f string
a=10
b=20
print("sum of",a,"and",b,"is :",a+b)
sum of 10 and 20 is : 30
#for reduce code by using above methods
print(f"sum of {a} and {b} is{a+b}")
sum of 10 and 20 is30
sum of 10 and 20 is30
SyntaxError: invalid syntax
print(f"sum of {a} and {b} is {a+b}")
sum of 10 and 20 is 30
sum of 10 and 20 is 3
print(f"sum of {a} and {b} is{a+b}")
SyntaxError: invalid syntax
print(f"sum of {a} and {b} is : {a+b}")
sum of 10 and 20 is : 30
c=30
d=40
print(f"sum of {c} and {d} is : {a+b}")
sum of 30 and 40 is : 30
sum of 30 and 40 is : 30
SyntaxError: invalid syntax
print(f"sum of {c} and {d} is : {c+d}")
sum of 30 and 40 is : 70
#for reduce code by using above methods
# using f string
a,b,c=10,20,30
print(f"sum of {a},{b},{c} is : {a+b+c}" )
sum of 10,20,30 is : 60
#--->using dot format
a,b=10,20
print("sum of{} and {} is {}".format(a,b,a+b))
