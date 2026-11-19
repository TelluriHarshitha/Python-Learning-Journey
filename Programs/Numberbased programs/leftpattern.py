'''program 
n=4
*
**
***
****
building by using both while and for loop'''

def leftpattern(n):
  for i in range(1,n+1):
    print('*'*i)
num=int(input("Enter the number of rows"))
leftpattern(num)

#by using while loop
rows=int(input("Enter number of rows"))
row_no=1
while row_no<=rows:
  print('*'*row_no)
  row_no=row_no+1


