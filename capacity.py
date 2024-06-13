#consider a disk has two surfaces,each sector is divided into b blocks.
#explaination:
#capacity=2*s*t*b*512 bytes.
#1kb=1024 bytes
#so,capacity in kb-->total capacity in bytes/1024
s=15
t=20
b=30
c=2*s*t*b*512
print(c/1024)
print("{:.0f} kb".format(c/1024))
print(c, "kb")
d=c/1024
print(d)
