'''program 
n=4
*
**
***
****
building by using both while and for loop'''

def leftpattern(n):
  for i in range(1,n+1):
    print(i)


num=int(input("Enter the number of rows"))
print(leftpattern(num))
