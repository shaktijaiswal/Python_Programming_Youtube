num=int(input("Enter the number : "))

temp=num
r=0
while(num>0):
    rem=num%10
    r=r*10+rem
    num=num//10
if(temp==r):
    print("this number is palindrome number")
else:
    print("this number is not palindrome")