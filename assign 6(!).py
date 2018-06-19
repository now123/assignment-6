#QUE1-
num = []
for i in range (0,10):
    num.append (int(input ("enter the no.")))
    print (num)

#QUE2-
while True:
    print ("true")

#QUE 3-
a=[]
b=[]
for i in range (0,4):
    number=int(input("enter the number"))
    a.append(number)
print(a)
for i in a:
    b.append(i**2)
print(b)


#QUE 4-
l = [1,"a",2.5]
intlist =[x for x in l if isinstance (x,int)]
print(intlist)
flist =[x for x in l if isinstance (x,float)]
print (flist)
strlist =[x for x in l if isinstance (x,str)]
print (strlist)

#QUE 5-
odd = []
even = []
for i in range (1,101):
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print ("even list",even)
print ("odd list",odd)


#QUE 6-

a = []
for i in range (0,4):
    for j in  range (0,i+1):
        print ("*" ,end=" ")
    print("\r")

#QUE 7-
list = {'tarun':25,'abhi':60}
search_age = input("provide age:")
search_age = int(search_age)
listofage = {}
for name , age in list.items():
        if age== search_age:
            age = str(age)
            results = name + " "+age
            print (results)

#QUE 8-
our_list = []
for i in range (0,5):
    number = int(input("enter the no."))
    our_list.append(number)
    print (our_list)
l2 = []
a= int(input("enter the no to be deleted"))
if a in our_list:
    print (a)
    x=our_list.index (a)
    x=our_list.remove(a)
print(our_list)


