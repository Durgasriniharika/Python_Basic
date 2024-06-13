#conditional statements or decision making statements
#1.if
#2.if-else
#3.if elif else
#4.nested if

#--->1. if
#syntax (if condition:)
#    statement 1 (we can write multiple statements)
#    statement 2
#ex:1
#a=10
#b=20
#if b>a:
    #print("b is largest number")
#print("hai")
      #print("hai")#indentation error
#even or odd
#n=int(input())
#if n%2==0:
  #print("n is even")
#print("odd")#(outside statement)

#--->2.if else(if condition true if block statement will execute otherwise else block statement will execute).
#syntax (if condition:)
#     statement 1
#     statement 2
# else:
# statement 1
# statement 2
#ex:1
#p=int(input())
#if p>=70:
   # print("join in b tech")
#else:
    #print("join in job")
#ex:2
#even or odd
#n=int(input())
#if n%2==0:
  #print("n is even")
#else:
    #print("odd")    
#without using else
    #even or odd
#n=int(input())
#if n%2==0:
  #print("n is even")
#if n%2!=0:
    #print("odd")
#--->3.if elif else:(used to print more than two conditions)
#syntax (if condition:)
  #statement 1
  #statement 2
#elif condition:
     #statement 1
     #statement 2
#elif condition:
     #statement 1
     #statement 2
#else
     #statement 1
     #statement 2
#ex:1
#largest number
    #f=int(input())
    #s=int(input())
    #t=int(input())
#if f>s and f>t:
    #print("f is largest number")
#elif s>f and s>t:
   # print("s is largest number")
#elif t>f and t>s:
    #print("t is largest number")
#else:("small")
#ex:2
#p=int(input())
#if p>80:
    #print("join in b tech")
#elif p<80 and p<60: #or 60<=n<=80
    #print("join in job")
#else:
    #print("join in coaching")
#--->4.nested if()
#syntax (if condition:)
           #if condition:
               #if condition:
                   #if condition;

#ex:1
#largest number
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print("a is largest number")
    else:
        print("c is largest number")
elif b>c:
    print("b is largest number")
else:
    print("c is largest number")
    
      
