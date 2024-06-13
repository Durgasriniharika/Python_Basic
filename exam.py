#django appeared for an exam consisting of 3 sections.each section is worth 100 marks.
#django scored A marks in section 1, B marks in section 2, c marks in section 3.
#django passes the exam if both of the following conditions satisfy:
# the total score of django is >=100
# score of each section >=10
#determine whether django passes the exam or not.
#a,b,c=map(int,input().split())
#if (a+b+c)>=100 and a>=10 and b>=10 and c>=10:
    #print("PASS")
#else:
   #print("FAIL")

#using nested if:
a,b,c=map(int,input().split())
if (a+b+c)>=100:
    if a>=10 and b>=10 and c>=10:
        print("PASS")
else:
    print("FAIL")
