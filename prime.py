#ask user for an integer and tell the user whether it is a prime number or not.  
mynum= int(input("Please enter an integer you want to check"))
isprime = True
i=2
while i < mynum:
     if (mynum % i)==0:
        isprime = False
        break
     i=i+1
      
if isprime == True:
     print(str(mynum) + " is a prime number")
else:
     print(str(mynum) + " is not a prime number")
