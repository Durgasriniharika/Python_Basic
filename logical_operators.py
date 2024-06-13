#logical operators
# 1.logical AND(&)#0,0---false,1,1----true
a=100
b=200
c=300
print(a>b and a<b)
print("{}>{} and {}<{}={}".format(a,b,a,b,a>b and a<b))
print(c>a & b<c)
# 2.logical OR(|)0,0---false,for remaining all true
print(a>b or a<b)
# 3.logical NOT(!)complement the output
print(not a<b)
# 4.assignment operator(=)
#swapping of values
a=10
b=20
print(a)
print(b)
a=b
b=a
print(a)
print(b)
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)
#another method to swap the values
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#explaination
b=30-10
b=20
#easy technique to swap in python
a,b=b,a
print(a,b,end='')#to print output in a single line
