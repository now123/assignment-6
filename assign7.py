#QUE 1-
radius = float (input("ente the no."))
def area (rad):
    area=3.14*rad*rad
    return area
a=area(radius)
print(a)
#QUE 2-

n=6
def perfect (n):
    sum=0
    for i in range (1,n):
        if (n%i==0):
         sum=sum+i
    if (sum == n):
         return True
    else:
         return False
print (perfect(n))
for i in range (1,1001):
        if (perfect(i)):
            print(i)
#que 3
def mul (n,i=1):
    print (i*n)
    if i!=10:
        mul(n,i+1)
print (mul(12))


#QUE4-
def power (a,b):
    if (b==1):
        return b
    else:
        return a*power(a,b-1)
print (power(2,4))

#QUE 5-
def fact(x):
    if (x<=1) :
        return 1
    else:
        return (x*fact(x-1))
x= int (input("enter the no"))
d={}
print ("fact")
print (fact(x))
d[x]=fact (x)
print (d)