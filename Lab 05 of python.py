#LAB5

#1
"""
x=int(input())
y=int(input())
n=int(input())
c=0
for i in range(x,y):
    if i%n!=0:
        print(i,end=" ")
        c=c+1
print()
print(c)
"""
#2
"""
n=int(input())
p=1
while n>0:
    d=n%10
    p=p*d
    n=n//10
print(p)
"""
#3
"""
n=int(input())
l=0
s=0
while True:
    b=int(input())
    if b==-999:
        break
    if b>n:
        l=l+1
    else:
        s=s+1
print(l)
print(s)
"""
#4
"""
n=int(input())
p=int(input())
if n<=0 or p<=0:
    print("invalid")
else:
    a=1
    i=1
    while i<=p:
        a=a*n
        i=i+1
    print(a)
"""
#5
"""
n=int(input())
m=int(input())
a=n
r=0
while a>0:
    d=a%10
    r=r*10+d
    a=a//10
if r==m:
    print("yes")
else:
    print("no")
"""
#6
"""
n=int(input())
a=1
i=1
while i<=n:
    print(a,end=" ")
    a=a*2
    i=i+1
"""
#7
"""
n=int(input())
if n<=0:
    print("invalid")
else:
    s=0
    i=1
    while i*i<=n:
        if n%i==0:
            s=s+i
            if i!=n//i:
                s=s+n//i
        i=i+1
    s=s-n
    if s==n:
        print("perfect")
    else:
        print("not perfect")
"""
#8
"""
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
"""
#9
"""
n=int(input())
d=int(input())
c=0
while n>0:
    a=n%10
    if a==d:
        c=c+1
    n=n//10
print(c)
"""
#10
"""
n=int(input())
c=0
i=1
while i*i<=n:
    if n%i==0:
        print(i)
        c=c+1
        if i!=n//i:
            print(n//i)
            c=c+1
    i=i+1
print(c)
if c==2:
    print("prime")
else:
    print("not prime")
"""
"""
x=int(input())
c=0
for j in range(1,x+1):
    if x%j==0:
        print(j)
        c+=1
print("Total divisors:",c)
if c==2:
    print("Prime number")
else:
    print("Not a prime number")
"""