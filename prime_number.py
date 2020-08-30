num=int(input("Enter the number : "))

# check prime number
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("this number is not prime")
            break
    else:
        print("this number is prime number")

else:
    print("this number is not prime number ")