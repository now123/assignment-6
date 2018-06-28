#QUE 1
#exception occcured is  ZeroDivisionError
try:
    a=3

    a=a/(a-3)
except ZeroDivisionError:
    print("error")
else:
    print(a)
finally:
    print("handeled")

#QUE-2
try:
    l = [1, 2, 3]
    print(l[3])
except IndexError:
    print("error")
finally:
    print("processed error")

#QUE-3

print("output is an exception")

#QUE 4-
output = "-5.0 a/b result in 0"
print(output)

#QUE5-
#import error
try:
    import tarun
except ImportError:
    print ("error")

#value error
try:
    n=int(input("enter"))
except ValueError:
    print("please enter an integer")
#index error
try:
    l=[1,2]
    n=l[4]
except IndexError:
    print("index out of bounds")

#QUE 6-
i=0
class Agetosmall(Exception):
    pass

while(i<18):
    try:
        i=int(input("E:"))
        if (i<18):
            raise Agetosmall

    except Agetosmall:
       print("age is less than 18")
else:
    while(False):
        pass






