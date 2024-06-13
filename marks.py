#given the marks(out of 100) 5 different subjects viz.english,maths,physics,chemistry,computer science.determine if the student passed or failed in exam.
#a student is considered pass if and only if he/she gets more than 34 marks in each?
a,b,c,d,e=map(int,input().split())
if (a>34) and (b>34) and (c>34) and (d>34) and (e>34):
    print("PASSED")
else:
    print("FAILED")
