a= int(input("Enter a number"))
c=0
n=0
while(a>0):
   
    n=a%10
    c+=1
    a//=10
print(f"The number of digits is {c}")
