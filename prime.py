myresult ='not a prime number'
mynum= 18
prime = True
i=2
while i < mynum:
     if (mynum % i)==0:
        prime = False
        break
     i=i+1
      
if prime == True:
     print(str(mynum) + " is a prime number")
else:
     print(str(mynum) + " is not a prime number")
