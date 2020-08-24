# fibonacci series
num=int(input("Enter the last number up to which series creates : "))
a=0
b=1
c=0
while(True):
    print(c, end=",")
    a=b
    b=c
    c=a+b
    if(c>num):
        break