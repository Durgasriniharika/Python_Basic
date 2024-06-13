#fatboy is fond of burgers and decided to make as many burgers as possible.fatboy has A patties and B buns.to make 1 burger,fatboy needs 1 patty and 1 bun.find the max number of burgers that fatboy can make?
p=int(input())
b=int(input())
if p==b: #p>=b
    print(b)
#else:
    #print(p)
elif p>b:
    print(b)
elif p<b:
    print(p)

