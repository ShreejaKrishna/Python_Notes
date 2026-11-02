a=[3,5,7,9]
b=[None]*len(a)
c1=0
n1=0
c2=0
n2=0
for i in range(len(a)):
  if i%2==0:
    b[i]=1
  else:
    b[i]=2
print(b)
for i in range(len(a)):
    if b[i]==1:
        c1=c1+1
        n1=n1+a[i]
    else:
        c2=c2+1
        n2=n2+a[i]

u1=n1/c1
u2=n2/c2
print(u1,u2)
