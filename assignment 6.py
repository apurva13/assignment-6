#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
pi=3.14
def area():
    r=int(input('Enter Radius:'))
    area=4*pi*r*r
    print('Area of Sphere:',area)
area()

#Q.2-Prints All the Perfect Numbers Between 1 and 1000

def perfect(n):
    add=0
    i=1
    while i<n:
        if(n%i==0):
            add=add+i
        i+=1
        
    if add==n and n!=1:
         print (n,'is a perfect number')

for i in range (1,1000):
    perfect(i)

#Q.3-Print Multiplication Table of a User Defined Number
def multiply(n):
    for x in range(1,11):
        print('{} x {} = {}'.format(n,x,n*x))

n=int(input('Enter integer:'))
multiply(n)
    
#Q.4-Calculate Power of a Number Using Recursion
def power(n,exp):
    if(exp==1):
        return n
    else:
        return n*power(n,exp-1)

n=int(input("Enter base: "))
exp=int(input("Enter exponential number: "))
res=power(n,exp)
print('Power of a number:',res)
