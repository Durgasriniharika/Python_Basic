#for the upcoming semester,the admins of thub decided to keep a total of x seats for the driveready course.student interest survey was conducted by the admins and it was found that y students were interested taking up the driveready course.
#find the minimum number of extra seats that the admins every student who is interested in taking the course would be able to do so.
x=int(input())
y=int(input())
if y<=x:
    print("0")
else:
    print("no.of seats required is",y-x)
